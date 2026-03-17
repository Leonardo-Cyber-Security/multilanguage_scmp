// Esempio PKCE + exchange token + chiamata start job (template)

// Utility PKCE
function base64UrlEncode(buffer) {
  return btoa(String.fromCharCode.apply(null, new Uint8Array(buffer)))
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
}

async function sha256(plain) {
  const encoder = new TextEncoder();
  const data = encoder.encode(plain);
  return await crypto.subtle.digest('SHA-256', data);
}

async function generateCodeChallenge(verifier) {
  const hashed = await sha256(verifier);
  return base64UrlEncode(hashed);
}

function generateCodeVerifier() {
  const array = new Uint8Array(32);
  crypto.getRandomValues(array);
  return Array.from(array).map(b => ('0' + b.toString(16)).slice(-2)).join('');
}

// Avvia il redirect per l'Authorization Code + PKCE
async function startAuth(cfg) {
  if (!cfg.clientId || !cfg.redirectUri || !cfg.orchestratorUrl) {
    alert('Inserisci client_id, orchestratorUrl e redirect_uri');
    return;
  }
  const codeVerifier = generateCodeVerifier();
  const codeChallenge = await generateCodeChallenge(codeVerifier);

  sessionStorage.setItem('pkce_code_verifier', codeVerifier);
  sessionStorage.setItem('auth_cfg', JSON.stringify(cfg));

  // ENDPOINTS: sostituisci con gli endpoint del tuo Orchestrator/Identity provider
  const authorizeEndpoint = `${cfg.orchestratorUrl}/oauth/authorize`;
  const params = new URLSearchParams({
    response_type: 'code',
    client_id: cfg.clientId,
    redirect_uri: cfg.redirectUri,
    code_challenge: codeChallenge,
    code_challenge_method: 'S256',
    scope: 'openid profile offline_access'
  });
  // aggiungi tenant se richiesto dall'implementazione locale
  window.location = `${authorizeEndpoint}?${params.toString()}`;
}

// Gestisce il redirect con ?code=...
async function handleRedirectCallback() {
  const url = new URL(window.location.href);
  const code = url.searchParams.get('code');
  if (!code) return;

  const cfg = JSON.parse(sessionStorage.getItem('auth_cfg') || '{}');
  const codeVerifier = sessionStorage.getItem('pkce_code_verifier');
  if (!cfg || !codeVerifier) {
    throw new Error('Missing PKCE state');
  }

  // Endpoint token: sostituire con l'endpoint reale
  const tokenEndpoint = `${cfg.orchestratorUrl}/oauth/token`;

  const body = new URLSearchParams({
    grant_type: 'authorization_code',
    code: code,
    redirect_uri: cfg.redirectUri,
    client_id: cfg.clientId,
    code_verifier: codeVerifier
  });

  const resp = await fetch(tokenEndpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: body.toString()
  });
  if (!resp.ok) throw new Error('Token request failed: ' + resp.status);
  const tokenData = await resp.json();
  sessionStorage.setItem('uipath_token', JSON.stringify(tokenData));

  // rimuovi il codice dalla query string per pulire l'URL
  url.searchParams.delete('code');
  window.history.replaceState({}, document.title, url.pathname + url.search);
}

async function loadTokenFromStorage() {
  return JSON.parse(sessionStorage.getItem('uipath_token') || '{}');
}

// Avvia job usando token (esempio generico). Adatta body e endpoint a seconda di On-Prem/Cloud.
async function startJobBrowser(accessToken, cfg, processKeyOrReleaseKey, inputArgumentsJson) {
  if (!accessToken) throw new Error('No access token');

  // Endpoint di esempio per StartJobs (sostituire secondo versione Orchestrator)
  const startJobsEndpoint = `${cfg.orchestratorUrl}/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs`;

  const body = {
    startInfo: {
      ReleaseKey: processKeyOrReleaseKey,
      Strategy: 'Specific',
      InputArguments: inputArgumentsJson || '{}'
    }
  };

  const resp = await fetch(startJobsEndpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + accessToken,
      'X-UIPATH-TenantName': cfg.tenant || ''
    },
    body: JSON.stringify(body)
  });
  if (!resp.ok) {
    const txt = await resp.text();
    throw new Error('Start job failed: ' + resp.status + ' - ' + txt);
  }
  return await resp.json();
}

// Elenca le Releases (processi) disponibili su Orchestrator
async function listTests(accessToken, cfg) {
  if (!accessToken) throw new Error('No access token');
  const endpoint = `${cfg.orchestratorUrl}/odata/Releases?$select=Key,Name,ProcessKey`;
  const resp = await fetch(endpoint, {
    method: 'GET',
    headers: {
      'Authorization': 'Bearer ' + accessToken,
      'X-UIPATH-TenantName': cfg.tenant || ''
    }
  });
  if (!resp.ok) {
    const txt = await resp.text();
    throw new Error('List releases failed: ' + resp.status + ' - ' + txt);
  }
  return await resp.json();
}

async function logout() {
  sessionStorage.removeItem('uipath_token');
  sessionStorage.removeItem('pkce_code_verifier');
  sessionStorage.removeItem('auth_cfg');
}

// helper per login.html
window.startAuth = startAuth;
window.handleRedirectCallback = handleRedirectCallback;
window.loadTokenFromStorage = loadTokenFromStorage;
window.startJobBrowser = startJobBrowser;
window.logout = logout;
window.listTests = listTests;
