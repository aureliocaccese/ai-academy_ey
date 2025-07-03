from py2neo import Graph, Node, Relationship
 
# Connessione a Neo4j (modifica user/pass se servono)
graph = Graph("bolt://localhost:7687", auth=("neo4j", "aurelio123"))
 
# Esempio di nodi
persona = Node("Persona", id="P001", nome="Mario", cognome="Rossi", ruolo="CEO")
azienda = Node("Azienda", id="A001", nome="ACME Srl", partitaIVA="12345678901")
documento = Node("Documento", id="D001", tipo="Contratto", importo=15000, data="2024-05-01")
 
# Esempio di relazioni
rel1 = Relationship(persona, "HA_FIRMATO", documento)
rel2 = Relationship(documento, "RIFERITO_A", azienda)
 
# Caricamento nel grafo
graph.create(persona | azienda | documento | rel1 | rel2)
 
print("Caricamento completato.")