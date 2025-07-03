from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aurelio123"))

# Vedi tutte le persone
print("Persone:")
for record in graph.run("MATCH (p:Persona) RETURN p"):
    print(record["p"])

# Vedi tutte le aziende
print("\nAziende:")
for record in graph.run("MATCH (a:Azienda) RETURN a"):
    print(record["a"])

# Vedi tutte le fatture
print("\nFatture:")
for record in graph.run("MATCH (f:Fattura) RETURN f"):
    print(record["f"])

# Vedi tutte le relazioni tra i nodi
print("\nRelazioni:")
for record in graph.run("MATCH (n)-[r]->(m) RETURN n, r, m"):
    print(record["n"], record["r"], record["m"])

# Query esempio: quante fatture sopra 10000 nel 2024?
print("\nFatture sopra 10k nel 2024:")
for record in graph.run("""
    MATCH (f:Fattura)
    WHERE f.importo > 10000 AND f.data STARTS WITH '2024'
    RETURN f.codice, f.importo, f.data
"""):
    print(record)