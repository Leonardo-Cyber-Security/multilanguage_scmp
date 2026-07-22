// main.js
// Carica la configurazione da config.js

async function authenticateWithExternalApp(secret, value) {
    const { orchestratorUrl, externalAppClientId } = orchestratorConfig;
    const response = await fetch(`${orchestratorUrl}/identity/connect/token`, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
            grant_type: 'client_credentials',
            client_id: externalAppClientId,
            client_secret: secret,
            value: value, // se serve, altrimenti rimuovi
            scope: 'OR.TestCases OR.TestCaseExecutions'
        })
    });
    if (!response.ok) throw new Error('Autenticazione fallita');
    const data = await response.json();
    return data.access_token;
}

async function fetchTestList(token) {
    const { orchestratorUrl } = orchestratorConfig;
    const res = await fetch(`${orchestratorUrl}/odata/TestCases`, {
        method: 'GET',
        mode: 'no-cors',
        headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) throw new Error('Errore nel recupero della lista test');
    const data = await res.json();
    return data.value;
}

async function startTest(token, testId) {
    const { orchestratorUrl, folderId } = orchestratorConfig;
    const startRes = await fetch(`${orchestratorUrl}/odata/TestCaseExecutions/UiPath.Server.Configuration.OData.StartTestCaseExecution`, {
        method: 'POST',
        mode: 'no-cors',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            testCaseId: testId,
            folderId: folderId // opzionale
        })
    });
    if (!startRes.ok) throw new Error('Errore nell\'avvio del test');
    return await startRes.json();
}

let cachedToken = null;

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('fetchTests').addEventListener('click', async function() {
        const secret = document.getElementById('secret').value;
        const value = document.getElementById('value').value;
        const resultDiv = document.getElementById('result');
        const testSelect = document.getElementById('testSelect');
        resultDiv.textContent = 'Caricamento lista test...';
        testSelect.innerHTML = '<option value="">-- Caricamento... --</option>';
        testSelect.disabled = true;
        document.getElementById('launchBtn').disabled = true;
        try {
            cachedToken = await authenticateWithExternalApp(secret, value);
            const tests = await fetchTestList(cachedToken);
            testSelect.innerHTML = '<option value="">-- Seleziona un test --</option>';
            tests.forEach(test => {
                const opt = document.createElement('option');
                opt.value = test.Id;
                opt.textContent = test.Name;
                testSelect.appendChild(opt);
            });
            testSelect.disabled = false;
            resultDiv.textContent = 'Lista test caricata.';
        } catch (err) {
            resultDiv.textContent = 'Errore: ' + err.message;
            testSelect.innerHTML = '<option value="">-- Carica la lista dei test --</option>';
            testSelect.disabled = true;
        }
    });

    document.getElementById('testSelect').addEventListener('change', function() {
        document.getElementById('launchBtn').disabled = !this.value;
    });

    document.getElementById('testForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        const testId = document.getElementById('testSelect').value;
        const resultDiv = document.getElementById('result');
        if (!cachedToken) {
            resultDiv.textContent = 'Effettua prima il login e carica la lista test.';
            return;
        }
        resultDiv.textContent = 'Avvio test...';
        try {
            await startTest(cachedToken, testId);
            resultDiv.textContent = 'Test avviato con successo!';
        } catch (err) {
            resultDiv.textContent = 'Errore: ' + err.message;
        }
    });
});
