from py2neo import Graph, Node, Relationship
import re

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aurelio123"))

# Esempio di entità estratte (normalmente da NER)
entities = [
    {"type": "Persona", "id": "PERSONA_001", "nome": "Mario", "cognome": "Rossi", "email": "mario.rossi@email.com"},
    {"type": "IBAN", "id": "IBAN_001", "iban": "IT60X0542811101000000123456"},
    {"type": "Indirizzo", "id": "INDIRIZZO_001", "via": "Via Roma 1", "citta": "Milano", "cap": "20100"}
]

# 1. Inserisci entità come nodi temporanei
for ent in entities:
    node = Node(ent["type"], **ent)
    graph.merge(node, ent["type"], "id")

# 2. Sostituisci nel testo originale
testo = "Mario Rossi ha IBAN IT60X0542811101000000123456 e abita in Via Roma 1, Milano."
testo_anon = testo
for ent in entities:
    if ent["type"] == "Persona":
        pattern = f"{ent['nome']} {ent['cognome']}"
    elif ent["type"] == "IBAN":
        pattern = ent["iban"]
    elif ent["type"] == "Indirizzo":
        pattern = f"{ent['via']}, {ent['citta']}"
    else:
        continue
    testo_anon = testo_anon.replace(pattern, f"[{ent['id']}]")

print("Testo anonimizzato:", testo_anon)

# 3. Funzione di ripristino
def ripristina_testo(testo_anon):
    def replace_id(match):
        ent_id = match.group(1)
        node = graph.nodes.match(id=ent_id).first()
        if not node:
            return match.group(0)
        if node["__primarylabel__"] == "Persona":
            return f"{node['nome']} {node['cognome']}"
        if node["__primarylabel__"] == "IBAN":
            return node["iban"]
        if node["__primarylabel__"] == "Indirizzo":
            return f"{node['via']}, {node['citta']}"
        return match.group(0)
    return re.sub(r"\[(\w+_\d+)\]", replace_id, testo_anon)

# Esempio di ripristino
testo_ripristinato = ripristina_testo(testo_anon)
print("Testo ripristinato:", testo_ripristinato)