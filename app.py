import streamlit as st
from openai import OpenAI
import random

st.set_page_config(page_title="The MET digital visit")

st.title("The MET digital visit")
st.write("Clique no botão abaixo para descobrir uma obra de arte real de um dos maiores museus do mundo")

if "artworks" not in st.session_state:
  st.session_state.artworks = []

if st.button("Mostrar uma nova obra"):
  try:
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
    data = response.json()
    object_ids = data["objectIDs"]
    while True:
      random.id = random.choice(object_ids)
      artwork = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/[random_id]").json()
      image_url = artwork.get("primaryImage", "")
      if image_url:
        break

title = artwork.get("title", "Titulo não disponível")
artist = artwork.get("artistDisplayName", "Artista desconhecido")
date = artwork.get("objectDate", "Data não informada")
st.session_state.artworks.append({
  "title": title,
  "artist": artist,
  "date": date,
  "image_url": image_url
})
except Exception as e:
st.error(f"Erro ao carregar a obra: {e}")

for art in reversed(st.session_state.artworks):
  st.image(art["image_url"], caption=f""{art['title']}" - {art['artist']} ({art['date']})", use_container_width=True)
  




      

                            

