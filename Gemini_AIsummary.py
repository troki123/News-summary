import os
from google import genai
from google.genai import types

# Inicijalizacija klijenta
client = genai.Client(api_key="AIzaSyDWllN6lo49dDa8JQWwzcPcL82NvrApVRo")

try:
    # Koristimo 'gemini-1.5-flash' jer je najstabilniji za besplatne ključeve
    # Maknuli smo 'models/' prefiks jer ga novi SDK sam dodaje
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents="Odgovori mi sa 'Bok!'"
    )
    
    if response.text:
        print("Uspjeh! AI kaže:")
        print(response.text)
    else:
        print("Odgovor je prazan (moguće zbog sigurnosnih filtera).")

except Exception as e:
    # Ako dobiješ 404 ovdje, problem je u postavkama prijateljevog projekta
    print(f"Greška: {e}")