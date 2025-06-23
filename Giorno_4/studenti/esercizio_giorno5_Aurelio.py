# azure_chat_test.py

import openai
import os

# Imposta le variabili d’ambiente manualmente qui (facoltativo, o usa .env/.bashrc)
os.environ["AZURE_OPENAI_KEY"] = "la-tua-api-key"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://nome-risorsa.openai.azure.com" 

# Inizializza il client AzureOpenAI
client = openai.AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-12-01-preview"
)

# Esegui la richiesta
response = client.chat.completions.create(
    model="o4-mini",  # Deployment name esatto definito nel portale Azure
    messages=[
        {"role": "system", "content": "Sei un assistente AI utile e conciso."},
        {"role": "user", "content": "Qual è la capitale dell'Italia?"}
    ],
    temperature=0.7,
    max_tokens=256
)

# Stampa la risposta del modello
print("Risposta:", response.choices[0].message.content)