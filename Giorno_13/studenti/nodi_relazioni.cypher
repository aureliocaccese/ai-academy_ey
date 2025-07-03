// Nodi
CREATE (p:Persona {nome: "Mario", cognome: "Rossi", ruolo: "Manager", partitaIVA: "RSSMRA80A01H501U"});
CREATE (a:Azienda {nome: "SmartDocs Srl", settore: "IT", partitaIVA: "12345678901"});
CREATE (f:Fattura {numero: "FAT2024-001", data: "2024-05-10", importo: 1500});
CREATE (c:Contratto {tipo: "Fornitura", data: "2024-01-15", importo: 5000});
CREATE (pr:Progetto {nome: "AI Platform", descrizione: "Sviluppo piattaforma AI"});
CREATE (iban:IBAN {codice: "IT60X0542811101000000123456"});
CREATE (e:Email {oggetto: "Invio Contratto", testo: "In allegato il contratto firmato", data: "2024-01-16"});
CREATE (d:Data {valore: "2024-01-15"});
CREATE (ind:Indirizzo {via: "Via Roma 1", citta: "Milano", CAP: "20100"});

// Relazioni con proprietà
CREATE (p)-[:HA_FIRMATO {timestamp: datetime("2024-01-15T10:00:00"), stato: "valido"}]->(c);
CREATE (f)-[:EMESSA_DA {timestamp: datetime("2024-05-10T09:00:00")}]->(a);
CREATE (p)-[:PARTECIPA_A {ruolo: "Project Manager"}]->(pr);
CREATE (e)-[:INVIATO_A {timestamp: datetime("2024-01-16T08:30:00")}]->(p);
CREATE (a)-[:USA_IBAN]->(iban);
CREATE (c)-[:DATA_FIRMA]->(d);
CREATE (a)-[:SEDE_LEGALE]->(ind);