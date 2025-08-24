# hello-cli

Una mini **Command Line Interface (CLI)** di esempio, utile per capire come strutturare un progetto open source in Python.

---

## 🚀 Funzionalità
- Stampa un saluto personalizzato via terminale.  
- Struttura del progetto completa: codice, test, documentazione, workflow GitHub Actions.  
- Perfetta come punto di partenza per nuovi progetti.

---

## ▶️ Utilizzo

Dopo l’installazione (vedi sotto), puoi eseguire:

```bash
hello-cli --name Marco
```

## Output:
Hello, Marco!

## Installazione:
# crea ambiente virtuale
python -m venv .venv

# attivalo
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux

# installa in modalità sviluppo
pip install -e .[dev]
