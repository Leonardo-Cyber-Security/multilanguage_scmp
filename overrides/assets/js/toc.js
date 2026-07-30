document.addEventListener("DOMContentLoaded", () => {
    // 1. Gestione ToC Secondaria (Fisarmonica e Scroll)
    document.querySelectorAll('.md-sidebar--secondary .md-nav__item').forEach(item => {
        const subList = item.querySelector(".md-nav__list");
        const link = item.querySelector(".md-nav__link");

        if (subList && link) {
            item.classList.add("has-children");
            
            link.addEventListener("click", (e) => {
                e.preventDefault();
                
                // Effetto fisarmonica: toggle visibilità
                const isVisible = subList.style.display === "block";
                subList.style.display = isVisible ? "none" : "block";
                item.classList.toggle("md-nav__item--active");

                // Smooth scroll verso la sezione
                const target = document.querySelector(link.getAttribute("href"));
                target?.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
        }
    });

    // 2. Correzione Link (Logo, Sidebar, Ancore) in un unico passaggio
    document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;

        let newHref = href;

        // Gestisce Logo e link relativi alla radice
        if (href === '.' || href === '..') {
            newHref = 'index.html';
        } 
        // Corregge index/index.html -> index.html
        else if (href.includes('index/index.html')) {
            newHref = href.replace('index/index.html', 'index.html');
        }
        // Corregge ancore path/#ancora -> path/index.html#ancora
        else if (href.match(/\/#[^/]+$/)) {
            newHref = href.replace('/#', '/index.html#');
        }
        // Aggiunge index.html a chi finisce con "/" (escluse ancore e root)
        else if (href.endsWith('/') && href.length > 1) {
            newHref = href + 'index.html';
        }

        if (newHref !== href) {
            link.setAttribute('href', newHref);
        }
    });

    // 3. Fix UI: Rimuove overflow forzato dalle tabelle
    document.querySelectorAll('.md-typeset__scrollwrap').forEach(wrap => {
        wrap.style.overflowX = 'visible';
    });
});
