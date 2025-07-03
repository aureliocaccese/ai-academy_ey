from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aurelio123"))

# Nodi
persona = Node("Persona", nome="Mario", cognome="Rossi", ruolo="Amministratore", partita_iva="RSSMRA80A01H501U")
azienda = Node("Azienda", nome="SmartDocs Srl", settore="IT", partita_iva="12345678901")
fattura = Node("Fattura", codice="Fattura123", data="2024-05-10", importo=1500.0, tipo="Vendita")
progetto = Node("Progetto", nome="AI Academy", descrizione="Corso di formazione AI")
iban = Node("IBAN", iban="IT60X0542811101000000123456")
email = Node("Email", indirizzo="mario.rossi@email.com")
data_firma = Node("Data", data="2024-05-11")
indirizzo = Node("Indirizzo", via="Via Roma 1", citta="Milano", cap="20100")

# Aggiungi nodi (evita duplicati se necessario)
graph.merge(persona, "Persona", "partita_iva")
graph.merge(azienda, "Azienda", "partita_iva")
graph.merge(fattura, "Fattura", "codice")
graph.merge(progetto, "Progetto", "nome")
graph.merge(iban, "IBAN", "iban")
graph.merge(email, "Email", "indirizzo")
graph.merge(data_firma, "Data", "data")
graph.merge(indirizzo, "Indirizzo", ("via", "citta", "cap"))

# Relazioni con proprietà
rel1 = Relationship(persona, "CLIENTE_DI", azienda, timestamp="2024-05-01T10:00:00", stato="attiva")
rel2 = Relationship(fattura, "EMESSA_DA", azienda, timestamp="2024-05-10T09:00:00")
rel3 = Relationship(fattura, "DESTINATARIO", persona)
rel4 = Relationship(persona, "PARTECIPA_A", progetto, ruolo="Studente", timestamp="2024-04-01T09:00:00")
rel5 = Relationship(email, "INVIATO_A", persona, timestamp="2024-05-09T08:00:00", motivazione="Invio fattura")
rel6 = Relationship(azienda, "USA_IBAN", iban)
rel7 = Relationship(fattura, "HA_INDIRIZZO", indirizzo)
rel8 = Relationship(fattura, "DATA_FIRMA", data_firma)

graph.merge(rel1)
graph.merge(rel2)
graph.merge(rel3)
graph.merge(rel4)
graph.merge(rel5)
graph.merge(rel6)
graph.merge(rel7)
graph.merge(rel8)

#KNOWLEDGE DATI AZIENDALI

# Vedi tutte le persone
for record in graph.run("MATCH (p:Persona) RETURN p"):
    print(record["p"])

# Vedi tutte le aziende
for record in graph.run("MATCH (a:Azienda) RETURN a"):
    print(record["a"])

# Vedi tutte le fatture
for record in graph.run("MATCH (f:Fattura) RETURN f"):
    print(record["f"])

# Vedi tutte le relazioni tra i nodi
for record in graph.run("MATCH (n)-[r]->(m) RETURN n, r, m"):
    print(record["n"], record["r"], record["m"])