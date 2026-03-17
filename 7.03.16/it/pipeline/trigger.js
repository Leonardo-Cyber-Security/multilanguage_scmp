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

// Avvia una pipeline YAML usando l'API runs
async function runPipeline(organization, project, pipelineId, pat, parametersJson) {
  if (!organization || !project || !pipelineId) throw new Error('Organization, Project e PipelineId richiesti');
  if (!pat) throw new Error('PAT mancante.');

  const url = `https://dev.azure.com/${encodeURIComponent(organization)}/${encodeURIComponent(project)}/_apis/pipelines/${encodeURIComponent(pipelineId)}/runs?api-version=7.1-preview.1`;

  let bodyObj = {};
  try {
    bodyObj = { resources: {}, templateParameters: JSON.parse(parametersJson || '{}') };
  } catch (e) {
    throw new Error('Parameters JSON non valido: ' + e.message);
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
      li.addEventListener('click', () => document.getElementById('pipelineId').value = p.id);
      listEl.appendChild(li);
    });
  } catch (e) {
    listEl.innerHTML = '<li>Errore: ' + e.toString() + '</li>';
  }
}

window.loadConfig = loadConfig;
window.loadAndShowPipelines = loadAndShowPipelines;
