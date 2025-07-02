# Documentazione Aurelio

**Categoria di rischio (Tier) – EU AI Act:**  
**ALTO (High-risk)**

---

## L'applicazione

- Analizza documenti aziendali contenenti potenzialmente dati personali, finanziari o legali.
- Prende decisioni o supporta processi aziendali automatizzati.

### Motivi della classificazione come High-Risk

- Rientra nella categoria dei sistemi AI utilizzati per gestire risorse umane o valutare informazioni di rilevanza legale o economica (Allegato III del regolamento).
- Coinvolge modelli generativi (GPT-4 in cloud) e modelli NLP locali (NER), quindi può influenzare decisioni umane e aziendali rilevanti.

---

| **Voce**                 | **Contenuto**                                                                              |
|--------------------------|--------------------------------------------------------------------------------------------|
| Finalità del trattamento | Analizzare documenti aziendali per identificare entità chiave e fornire risposte automatiche|
| Tecnologie impiegate     | Modello NER locale + GPT-4 (API cloud – OpenAI via Azure)                                  |
| Tipi di dati trattati    | Testi contenenti dati personali, nomi, ruoli, date, informazioni contrattuali o legali      |
| Categorie di interessati | Dipendenti, clienti, collaboratori, fornitori                                              |
| Modalità di trattamento  | Automatico, con log e supervisione umana a posteriori                                      |
| Base giuridica           | Interesse legittimo dell’azienda / Contrattuale                                            |

---

### Valutazione dei rischi

| **Rischio identificato**                        | **Probabilità** | **Impatto** | **Livello di rischio** | **Misure previste**                                      |
|-------------------------------------------------|-----------------|-------------|-----------------------|----------------------------------------------------------|
| Allucinazioni GPT (errori nel contenuto)        | Medio           | Alto        | Alto                  | Supervisione umana, filtro semantico                     |
| Identificazione errata entità (NER)             | Medio           | Medio       | Medio                 | Validazione manuale in fase di test                      |
| Accesso non autorizzato ai dati                 | Basso           | Alto        | Medio                 | Crittografia, controlli accesso, tokenization            |
| Uso improprio dei dati da parte del provider cloud | Basso         | Alto        | Medio                 | Verifica contrattuale (DPA con Azure/OpenAI)             |
| Violazione GDPR (es. mancata informazione utenti) | Medio          | Medio       | Medio                 | Notifiche trasparenti, privacy notice, diritto di opposizione |

###

- ✅ Il trattamento è necessario per velocizzare la gestione documentale.
- ✅ Sono adottate misure di minimizzazione, es. anonimizzazione dove possibile.
- ✅ È prevista sorveglianza umana per correggere risposte non conformi.
