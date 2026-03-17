// Helper per Azure DevOps REST con PAT (esempio)

function getAuthHeader(pat) {
  // Basic auth: base64 of ":{PAT}"
  const token = btoa(':' + pat);
  return 'Basic ' + token;
}

async function listPipelines(organization, project, pat) {
  if (!organization || !project) throw new Error('Organization e Project richiesti');
  if (!pat) throw new Error('PAT mancante. Salvalo in sessionStorage prima.');
  const url = `https://dev.azure.com/${encodeURIComponent(organization)}/${encodeURIComponent(project)}/_apis/pipelines?api-version=7.1-preview.1`;
  const resp = await fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': getAuthHeader(pat),
      'Content-Type': 'application/json'
    }
  });
  if (!resp.ok) {
    const txt = await resp.text();
    throw new Error('List pipelines failed: ' + resp.status + ' - ' + txt);
  }
  return await resp.json();
}

// Recupera dettagli del pipeline (per ottenere repository/id)
async function getPipelineDetails(organization, project, pipelineId, pat) {
  if (!organization || !project || !pipelineId) throw new Error('Organization, Project e PipelineId richiesti');
  const url = `https://dev.azure.com/${encodeURIComponent(organization)}/${encodeURIComponent(project)}/_apis/pipelines/${encodeURIComponent(pipelineId)}?api-version=7.1-preview.1`;
  const resp = await fetch(url, {
    method: 'GET',
    headers: { 'Authorization': getAuthHeader(pat), 'Content-Type': 'application/json' }
  });
  if (!resp.ok) {
    const txt = await resp.text();
    throw new Error('Get pipeline details failed: ' + resp.status + ' - ' + txt);
  }
  return await resp.json();
}

// Carica i branch per il repository associato al pipeline e popola la select
async function loadBranchesForPipeline(organization, project, pipelineId, pat) {
  const select = document.getElementById('branchSelect');
  select.innerHTML = '<option value="">Caricamento...</option>';
  try {
    const details = await getPipelineDetails(organization, project, pipelineId, pat);
    // tentiamo di trovare repository id
    let repoId = null;
    if (details && details.configuration && details.configuration.repository) {
      repoId = details.configuration.repository.id || details.configuration.repository.name || null;
    }
    // Se non troviamo repoId, proviamo a leggere dalla proprietà repository in cima
    if (!repoId && details && details.repository) {
      repoId = details.repository.id || details.repository.name || null;
    }

    if (!repoId) {
      // fallback: chiedi all'utente di inserire manualmente il repo (non ideale)
      select.innerHTML = '<option value="">Nessun repository associato trovato</option>';
      return;
    }

    // Chiamata per elencare refs (heads)
    const refsUrl = `https://dev.azure.com/${encodeURIComponent(organization)}/_apis/git/repositories/${encodeURIComponent(repoId)}/refs?filter=heads/&api-version=7.1-preview.1`;
    const refsResp = await fetch(refsUrl, { method: 'GET', headers: { 'Authorization': getAuthHeader(pat) } });
    if (!refsResp.ok) {
      const txt = await refsResp.text();
      throw new Error('List refs failed: ' + refsResp.status + ' - ' + txt);
    }
    const refsData = await refsResp.json();
    select.innerHTML = '';
    if (!refsData || !refsData.value || refsData.value.length === 0) {
      select.innerHTML = '<option value="">Nessun branch trovato</option>';
      return;
    }
    refsData.value.forEach(r => {
      const name = (r.name || '').replace('refs/heads/', '');
      const opt = document.createElement('option');
      opt.value = name;
      opt.textContent = name;
      select.appendChild(opt);
    });
  } catch (e) {
    select.innerHTML = '<option value="">Errore caricamento branch</option>';
    console.error(e);
  }
}


// Avvia una pipeline YAML usando l'API runs
async function runPipeline(organization, project, pipelineId, pat, parametersJson) {
  if (!organization || !project || !pipelineId) throw new Error('Organization, Project e PipelineId richiesti');
  if (!pat) throw new Error('PAT mancante.');

  const url = `https://dev.azure.com/${encodeURIComponent(organization)}/${encodeURIComponent(project)}/_apis/pipelines/${encodeURIComponent(pipelineId)}/runs?api-version=7.1-preview.1`;

  let bodyObj = {};
  let templateParams = {};
  try {
    templateParams = JSON.parse(parametersJson || '{}');
  } catch (e) {
    throw new Error('Parameters JSON non valido: ' + e.message);
  }

  // Se è selezionato un branch, includilo nelle risorse
  const branch = (document.getElementById('branchSelect') && document.getElementById('branchSelect').value) || '';
  if (branch) {
    bodyObj = { resources: { repositories: { self: { refName: `refs/heads/${branch}` } } }, templateParameters: templateParams };
  } else {
    bodyObj = { resources: {}, templateParameters: templateParams };
  }
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': getAuthHeader(pat),
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(bodyObj)
  });
  if (!resp.ok) {
    const txt = await resp.text();
    throw new Error('Run pipeline failed: ' + resp.status + ' - ' + txt);
  }
  return await resp.json();
}

// Esporta le funzioni per uso in trigger.html
window.listPipelines = listPipelines;
window.runPipeline = runPipeline;

// Carica config.json (defaults) dalla stessa cartella e applica ai campi della pagina
async function loadConfig() {
  try {
    const resp = await fetch('config.json');
    if (!resp.ok) return {};
    const cfg = await resp.json();
    if (cfg.organization) document.getElementById('organization').value = cfg.organization;
    if (cfg.project) document.getElementById('project').value = cfg.project;
    if (cfg.defaultPipelineId) document.getElementById('pipelineId').value = cfg.defaultPipelineId;
    if (cfg.defaultParameters) document.getElementById('parameters').value = JSON.stringify(cfg.defaultParameters);
    return cfg;
  } catch (e) {
    console.warn('Impossibile caricare config.json:', e);
    return {};
  }
}

// Carica e mostra la lista delle pipeline (usa i campi della pagina)
async function loadAndShowPipelines() {
  const org = document.getElementById('organization').value;
  const proj = document.getElementById('project').value;
  const pat = sessionStorage.getItem('azure_pat');
  const listEl = document.getElementById('pipelinesList');
  if (!listEl) return;
  listEl.innerHTML = 'Caricamento...';
  try {
    const data = await listPipelines(org, proj, pat);
    listEl.innerHTML = '';
    if (!data || !data.value || data.value.length === 0) {
      listEl.innerHTML = '<li>Nessuna pipeline trovata</li>';
      return;
    }
    data.value.forEach(p => {
      const li = document.createElement('li');
      li.textContent = `${p.name} (id: ${p.id})`;
      li.style.cursor = 'pointer';
      li.addEventListener('click', async () => {
        document.getElementById('pipelineId').value = p.id;
        try {
          await loadBranchesForPipeline(org, proj, p.id, pat);
        } catch (e) {
          console.error('Errore caricamento branch:', e);
        }
      });
      listEl.appendChild(li);
    });
  } catch (e) {
    listEl.innerHTML = '<li>Errore: ' + e.toString() + '</li>';
  }
}

window.loadConfig = loadConfig;
window.loadAndShowPipelines = loadAndShowPipelines;
window.loadBranchesForPipeline = loadBranchesForPipeline;
