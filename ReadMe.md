<h1>
    Demarrer un projet Django + Tailwind CSS
</h1>
<a href="https://www.docstring.fr/blog/utiliser-tailwind-css-dans-un-projet-django/"> Site docstring </a>
<ol>
    <li> Mise en place de l'environnement Django
        <ul>
            <li><code>mkdir django_tailwind && cd django-tailwind</code></li>
            <li><code>py -3 -m venv py-env</code></li>
            <li><code>source py-env/Scripts/activate</code></li>
            <li><code>pip install django</code></li>
        </ul>
    </li>
    <li> Installation de tailwind
        <ul>
            <li>Installer Node.js et nm</li>
            <li><code>pip install django-tailwind</code></li>
        </ul>
    </li>
    <li><code>django-admin startproject website</code></li>
    <li><code>py -3 manage.py runserver</code></li>
    <li>Ajouter <code>'tailwind'</code> dans la liste d'application (INSTALLED_APS)</li>
    <li>Créer l'application qui contiendra tous les fichiers pour faire fonctionner tailwind
        <ul>
            <li><code>py -3 manage.py tailwind init</code> : ce processus demandera le nom de l'application. Par defaut le nom 'theme' est utilisé </li>
            <li>Ajouter <code>'theme'</code>  dans la liste d'application de <code>settings.py</code></li>
            <li>ajouter <code>TAILWIND_APP_NAME = 'theme'</code> dans <code>settings.py</code></li>
            <li>ajouter <code>INTERNAL_IPS = ["127.0.0.1"]</code> dans <code>settings.py</code></li>
        </ul>
    </li>
    <li>Pour finir, il faut installer toutes les dependances javascript nécessaire avec la commande 
    <code>py -3 manage.py tailwind install</code></li>
    <li>Inclure tailwind dans le gabarit html
        <ul>
            <li>En haut du fichier HTML, idéalement <code>base.html</code>, il faut charger 
            <code>{% load tailwind_tags %}</code></li>
            <li> A l'interieur de la balise <code>head</code>, il faut inclure <code>tailwind_css</code></li>
        </ul>
    </li>
    <li> dans un terminal il faut lancer <code>py -3 manage.py tailwind start</code></li>
    <li> Par defaut, seuls les fichiers HTML à l'interieur des différents dossiersde templates de Django sont pris en compte. Heureusement, il est possible de modifier cett configuration en modifiant la clé 'purge' dans le fichier <code>tailwind.config.js</code> qui se trouve dans l'application theme à l'interieur du dossier static_src.
    Si jamais vous utilisez des classes tailwind à l'interieur d'un fichier Js ou py, n'oubliez pas d'enlever des commentaires sur les lignes correspondantes : <code>'../../**/*.js' et '../../**/*.py'</code></li>
    <li>Assurez-vous de lancer le serveur de développement de tailwind avec la commande <code>py -3 manage.py tailwind start</code>.C'est ce serveur qui va scanner tous les fichiers de votre projet pour vérifier quelle classe de Tailwind vous utilisez et les ajouter au fichier CSS final. Ce processus est réalisé pour éviter de charger l'intégralité des classes de Tailwind CSS dans votre projet. Assurez-vous également comme nous l'avons vu ci-dessus, de modifier le fichier de purge s jamais vous utlisez des classes Tailwind da,ns des fichiers js ou py </li>
</ol>


<h1>
    Configuration du mode nuit/jour dans un projet Django + Tailwind CSS
</h1>

<h3> Ajouter ce code dans le head </h3>
<code>
    <!-- Sur chargement de la page ou hangement de theme-->
    <script>
        if(localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)){
            document.documentElement.classList.add('dark');
        }    
        else{
            document.documentElement.classList.remove('dark');
        }
    </script>
</code>

<h3>Ajouter ce bouton dans l'entete </h3>
<code>
     <button id="theme-toggle" type="button" class="text-gray-500 border dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5">
        <span id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">dark</span>
        <span id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">light</span>
    </button>
</code>

<h3> Ajouter ce script dans votre fichier principal pour utiliser le bouton de changement d'etat </h3>
<code>
<script> 
        //Code pour dynamiser le bouton de changement du mode
        var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon')
        var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon')
        //Changer l'icone du bouton
        if(localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)){
            themeToggleLightIcon.classList.remove('hidden');
        }
        else{
            themeToggleDarkIcon.classList.remove('hidden');
        }
        var themeToggleBtn = document.getElementById('theme-toggle');
        themeToggleBtn.addEventListener('click', function(){
            // Toggle icons inside button
            themeToggleDarkIcon.classList.toggle('hidden');
            themeToggleLightIcon.classList.toggle('hidden');
            // if set via local storage priviously
            if (localStorage.getItem('color-theme')){
                if (localStorage.getItem('color-theme') === 'light'){
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
                else{
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                }
            }
            // if not set via local storage previously
            else{
                if(document.documentElement.classList.contains('dark')){
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                }
                else{
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
            }
        })
    </script>
</code>