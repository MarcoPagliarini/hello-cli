# Contribuire

Grazie per il tuo interesse! Per proporre modifiche:

1. Fai un **fork** della repo e crea un branch: `feat/nome-feature`.
2. Segui gli standard di stile (formattazione automatica).
3. Aggiungi o aggiorna i **test** se servono.
4. Apri una **Pull Request** ben descritta (vedi template).

## Setup dev
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```
Stile

Usa formattazione automatica (black) e lint (ruff).

I test devono passare (pytest).

Grazie! 🙏
