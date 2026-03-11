// Language Switcher JavaScript - Dynamic Injection
document.addEventListener('DOMContentLoaded', function() {
    // Forza redirect a /it/ se manca prefisso lingua
    setTimeout(function() {
        const path = window.location.pathname;
        // helper disponibile anche globalmente (dichiarata più sotto)

        if (!/^\/(it|en)\//.test(path)) {
            const newPath = insertLangBeforeFolder(path, 'it');
            const newUrl = window.location.origin + newPath + window.location.search + window.location.hash;
            window.location.replace(newUrl);
            return;
        }
        injectLanguageSwitcher();
    }, 100);
});

// helper: inserisce il prefisso lingua prima della cartella che contiene index.html
function insertLangBeforeFolder(originalPath, lang) {
    const parts = originalPath.split('/').filter(Boolean);
    if (parts.length === 0) return `/${lang}/`;
    let pos;
    if (parts[parts.length - 1].toLowerCase() === 'index.html') {
        pos = parts.length - 2; // prima della cartella che contiene index.html
    } else {
        pos = parts.length - 1; // prima dell'ultima cartella
    }
    if (pos < 0) pos = 0;
    parts.splice(pos, 0, lang);
    return '/' + parts.join('/');
}

function injectLanguageSwitcher() {
    // Trova la navbar dell'header di Material
    const headerNav = document.querySelector('.md-header__inner');
    if (!headerNav) {
        console.log('Header nav not found, retrying...');
        setTimeout(injectLanguageSwitcher, 200);
        return;
    }

    // Controlla se il language switcher è già stato aggiunto
    if (document.getElementById('language-switcher')) {
        console.log('Language switcher already exists');
        return;
    }

    // Crea il language switcher
    const languageSwitcherContainer = document.createElement('div');
    languageSwitcherContainer.className = 'md-header__option';
    languageSwitcherContainer.innerHTML = `
        <div class="md-select">
            <button class="md-select__button md-icon" id="language-switcher" title="Switch Language">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: 1.2rem; height: 1.2rem; fill: currentColor;">
                    <path d="M12.87 15.07L10.33 12.56L10.36 12.53C12.1 10.59 13.34 8.36 14.07 6H17V4H10V2H8V4H1V6H12.17C11.5 7.92 10.44 9.75 9 11.35C8.07 10.32 7.3 9.19 6.69 8H4.69C5.42 9.63 6.42 11.17 7.67 12.56L2.58 17.58L4 19L9 14L12.11 17.11L12.87 15.07M18.5 10H16.5L12 22H14L15.12 19H19.87L21 22H23L18.5 10M15.88 17L17.5 12.67L19.12 17H15.88Z"/>
                </svg>
            </button>
            <div class="md-select__inner" id="language-menu" style="display: none;">
                <div class="md-select__list">
                    <a href="#" class="md-select__item" id="switch-to-it">
                        <span class="md-select__text">🇮🇹 Italiano</span>
                    </a>
                    <a href="#" class="md-select__item" id="switch-to-en">
                        <span class="md-select__text">🇬🇧 English</span>
                    </a>
                </div>
            </div>
        </div>
    `;

    // Trova dove inserire il language switcher (prima del repo source se presente, altrimenti alla fine)
    const sourceElement = headerNav.querySelector('.md-header__source');
    if (sourceElement) {
        headerNav.insertBefore(languageSwitcherContainer, sourceElement);
    } else {
        headerNav.appendChild(languageSwitcherContainer);
    }

    // Ora collega gli event listeners
    setupLanguageSwitcherEvents();
    console.log('Language switcher injected successfully');
}

function setupLanguageSwitcherEvents() {
    const languageSwitcher = document.getElementById('language-switcher');
    const languageMenu = document.getElementById('language-menu');
    const switchToIt = document.getElementById('switch-to-it');
    const switchToEn = document.getElementById('switch-to-en');
    
    if (!languageSwitcher || !languageMenu || !switchToIt || !switchToEn) {
        console.log('Language switcher elements not found after injection');
        return;
    }

    // Toggle menu visibility
    languageSwitcher.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        languageMenu.style.display = languageMenu.style.display === 'none' ? 'block' : 'none';
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!languageSwitcher.contains(e.target)) {
            languageMenu.style.display = 'none';
        }
    });

    // Get current URL and detect language
    function getCurrentLanguage() {
        const path = window.location.pathname;
        if (path.includes('/en/')) {
            return 'en';
        } else if (path.includes('/it/')) {
            return 'it';
        }
        // Default fallback - check if we're in a subdirectory structure
        return 'it'; // Default to Italian
    }


    
    function switchLanguage(targetLang) {
        const currentLang = getCurrentLanguage();
        let path = window.location.pathname;
        if (currentLang === targetLang) return;

        // Sostituisci solo il segmento lingua se presente
        if (/^\/(it|en)\//.test(path)) {
            path = path.replace(/^\/(it|en)\//, `/${targetLang}/`);
        } else {
            // Se non c'è prefisso lingua, inseriscilo prima della cartella che contiene index.html (o prima dell'ultima cartella)
            path = insertLangBeforeFolder(path, targetLang);
        }
        // Normalizza doppie barre
        path = path.replace(/\/\//g, '/');
        const newUrl = window.location.origin + path;
        console.log(`Switching from ${currentLang} to ${targetLang}: ${newUrl}`);
        window.location.href = newUrl;
    }


    switchToIt.addEventListener('click', function(e) {
        e.preventDefault();
        switchLanguage('it');
    });

    switchToEn.addEventListener('click', function(e) {
        e.preventDefault();
        switchLanguage('en');
    });

    // Update button text based on current language
    function updateSwitcherText() {
        const currentLang = getCurrentLanguage();
        const button = languageSwitcher;
        
        // Hide current language option
        if (currentLang === 'it') {
            switchToIt.style.display = 'none';
            switchToEn.style.display = 'block';
            button.title = 'Switch to English';
        } else {
            switchToIt.style.display = 'block';
            switchToEn.style.display = 'none';
            button.title = 'Passa all\'Italiano';
        }
    }

    // Initialize
    updateSwitcherText();
}