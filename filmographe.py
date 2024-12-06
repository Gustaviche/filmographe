import streamlit as st
from streamlit_option_menu import option_menu

# Données des utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'Administrateur',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Fonction pour vérifier les identifiants
def verifier_identifiants(username, password):
    if username in lesDonneesDesComptes['usernames']:
        user = lesDonneesDesComptes['usernames'][username]
        if password == user['password']:
            return True, user['name'], user['role']
    return False, None, None


# Interface de connexion
def connexion():
    st.sidebar.title("Connexion")
    username = st.sidebar.text_input("Nom d'utilisateur")
    password = st.sidebar.text_input("Mot de passe", type="password")
    if st.sidebar.button("Se connecter"):
        auth_status, name, role = verifier_identifiants(username, password)
        if auth_status:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.name = name
            st.session_state.role = role
            st.sidebar.success(f"Bienvenue, {name}!")
        else:
            st.sidebar.error("Identifiants incorrects.")
    else:
        st.sidebar.info("Veuillez entrer vos identifiants.")


# Déconnexion
def deconnexion():
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.name = None
    st.session_state.role = None
    st.sidebar.success("Vous êtes maintenant déconnecté.")


# Gestion des états de session
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.name = None
    st.session_state.role = None

# Si l'utilisateur est connecté
if st.session_state.authenticated:
    st.sidebar.success(f"Connecté en tant que : {st.session_state.name}")
    if st.sidebar.button("Se déconnecter"):
        deconnexion()

    # Menu de navigation
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Films", "Déconnexion"],
        icons=["house-door", "film", "box-arrow-right"],
        default_index=0
    )

    # Pages de l'application
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil")
        st.write("Voici une application protégée par une authentification.")
    elif selection == "Films":
        st.title("Mes Films Récents")
        st.write("Voici une sélection de films que j'ai vus récemment.")

        # Galerie de films
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://fr.web.img6.acsta.net/c_310_420/img/e7/a7/e7a7487a5131819d19b58f43718336b1.jpg", caption="Heretic")
            st.write("Bof")

        with col2:
            st.image("https://fr.web.img2.acsta.net/img/dc/5e/dc5e71f5a015d5d24f0135ee600ac27b.jpg", caption="The Substance")
            st.write("Sympa")

        with col3:
            st.image("https://fr.web.img6.acsta.net/img/29/eb/29eb8341475fdb0b19b1d7b995b70e17.jpg", caption="Le Compte de Monte-Cristo")
            st.write("Cool")

        st.write("---")

        col4, col5, col6 = st.columns(3)

        with col4:
            st.image("https://fr.web.img6.acsta.net/img/3b/fc/3bfc5635c5724bd83392c3a9b541fff9.jpg", caption="Speak No Evil")
            st.write("Strange")

        with col5:
            st.image("https://fr.web.img3.acsta.net/img/aa/f4/aaf4c61052ffc2a8056eee68681b1832.jpg", caption="Alien : Romulus")
            st.write("Sans plus")

        with col6:
            st.image("https://fr.web.img4.acsta.net/img/d5/8d/d58d37b3954c13d22a366da5721842cb.jpg", caption="Blink Twice")
            st.write("Très Cool")

    elif selection == "Déconnexion":
        deconnexion()

# Si l'utilisateur n'est pas connecté
else:
    connexion()
