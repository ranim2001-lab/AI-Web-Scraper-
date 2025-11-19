import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# --------------------------
#   STREAMLIT UI
# --------------------------

st.title("🔎 Web Scraper – Streamlit Demo")
url = st.text_input("Entrez une URL à scraper:")

# --------------------------
#   1) SCRAPING
# --------------------------

if st.button("Scrape"):
    if url:
        st.info("⏳ Scraping en cours...")

        try:
            # Désactiver le proxy pour charger la vraie page
            html = scrape_website(url, use_proxy=False)

            st.success("✔ HTML récupéré !")

            # 1) Afficher HTML brut
            st.subheader("📄 HTML brut (les 500 premiers caractères)")
            st.code(html[:500])

            # 2) Extraction du <body>
            body = extract_body_content(html)

            st.subheader("🌿 <body> extrait (first 500 chars)")
            st.code(body[:500] if body else "Aucun body détecté")

            # 3) Nettoyage
            cleaned = clean_body_content(body)

            st.subheader("🧼 Texte nettoyé")
            st.text_area("Contenu extrait", cleaned, height=250)

            # Sauvegarde dans Session State
            st.session_state.dom_content = cleaned

        except Exception as e:
            st.error(f"Erreur scraping : {e}")

    else:
        st.error("Veuillez entrer une URL.")

# --------------------------
#   2) PARSING VIA OLLAMA
# --------------------------

if "dom_content" in st.session_state:

    st.subheader("✍ Décrivez ce que vous voulez parser")
    request = st.text_area(
        "Exemples :\n- Extrais tous les titres H2\n- Donne un résumé\n- Mets le contenu dans un tableau\n- Liste toutes les dates\n",
        height=150
    )

    if st.button("Parse Content"):
        if request:
            st.info("🤖 Parsing via Ollama...")

            try:
                # Découpage en chunks si texte long
                chunks = split_dom_content(st.session_state.dom_content)

                # Appel LLM avec ton fichier parse.py
                result = parse_with_ollama(chunks, request)

                st.subheader("📌 Résultat du parsing")
                st.write(result)

            except Exception as e:
                st.error(f"Erreur parsing : {e}")

        else:
            st.error("Décrivez ce que vous voulez parser.")
