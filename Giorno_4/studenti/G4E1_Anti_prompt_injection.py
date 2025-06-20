def valida_prompt(prompt):
    """
    Controlla il prompt prima di inviarlo al modello, per prevenire injection o abusi.
    """
    # 1. Lista di parole/frasi da bloccare
    blacklist = [
        "ignora istruzioni",
        "resetta ruolo",
        "password",
        "override",
        "inizia come",
        "dimentica",
        "disattiva",
        "act as",
        "system:",
        "assistant:",
        "ignore previous",
        "jailbreak"
        # Puoi aggiungere altri termini sospetti qui
    ]
    
    # 2. Controllo presenza parole vietate (case-insensitive)
    prompt_lower = prompt.lower()
    for parola in blacklist:
        if parola in prompt_lower:
            raise ValueError(f"Prompt bloccato: contiene la parola vietata '{parola}'")
    
    # 3. (FACOLTATIVO) Limite sulla lunghezza del prompt
    max_length = 400  # esempio: massimo 400 caratteri
    if len(prompt) > max_length:
        raise ValueError("Prompt troppo lungo")

    # 4. (FACOLTATIVO) Altri controlli (esempi)
    if "${" in prompt or "}}}" in prompt:
        raise ValueError("Prompt contiene variabili non sicure.")

    # Se supera tutti i controlli
    return True

# Esempio d’uso
if __name__ == "__main__":
    prompt_utente = input("Inserisci il prompt da controllare: ")
    try:
        if valida_prompt(prompt_utente):
            print("✅ Prompt accettato. Procedo con l’invio al modello.")
    except ValueError as e:
        print("❌ Errore:", e)
