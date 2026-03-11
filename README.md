# IWG-400: Git, Python, Google Trends y Monte Carlo

Material base para la actividad en clases de IWG-400.

## Que incluye este repositorio

- `docs/actividad01_en_clases_setup_git_notebooks_trends_montecarlo.pdf`: guia de la actividad.
- `scripts/fetch_google_trends.py`: descarga datos de Google Trends y los guarda en CSV.
- `notebooks/00_descargar_google_trends.ipynb`: version notebook del paso de descarga.
- `notebooks/01_analisis_trends.ipynb`: analisis inicial de series temporales con `pandas`.
- `notebooks/02_montecarlo_pi.ipynb`: simulacion de Monte Carlo para aproximar `pi`.
- `data/`: carpeta donde se guarda `google_trends.csv`.
- `requirements.txt`: dependencias minimas del proyecto.

## Flujo recomendado

1. Crear y activar un entorno virtual `.venv`.
2. Instalar dependencias con `pip install -r requirements.txt`.
3. Descargar datos reales de Google Trends.
4. Ejecutar `notebooks/01_analisis_trends.ipynb`.
5. Ejecutar `notebooks/02_montecarlo_pi.ipynb`.
6. Guardar cambios con Git.

## Setup rapido

### Windows

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Descargar datos reales de Google Trends

### Opcion 1: script

```bash
python scripts/fetch_google_trends.py \
  --keywords ChatGPT TikTok Instagram \
  --geo CL \
  --timeframe "today 3-m" \
  --output data/google_trends.csv
```

### Opcion 2: notebook

Abrir y ejecutar:

```text
notebooks/00_descargar_google_trends.ipynb
```

## Nota importante sobre Google Trends

Google Trends no ofrece una API publica oficial documentada para este uso en el material revisado. Por eso este repositorio usa `pytrends`, que es una libreria no oficial que automatiza consultas al servicio de Trends.

Esto implica dos cosas:

- puede romperse si Google cambia su interfaz;
- conviene mantener un plan B de exportacion manual en CSV.

Si la descarga automatica falla, puedes usar la exportacion manual desde la web de Google Trends y guardar el archivo como `data/google_trends.csv`.

## Publicar en GitHub

Cuando `gh` este autenticado correctamente:

```bash
git init
git add .
git commit -m "feat: actividad inicial con trends y monte carlo"
gh repo create iwg400-actividad01-trends-montecarlo --public --source=. --remote=origin --push
```

## Fuentes y referencias

- VS Code: <https://code.visualstudio.com/>
- Python 3.12.10: <https://www.python.org/downloads/release/python-31210/>
- Git: <https://git-scm.com/>
- Google Trends: <https://trends.google.com/>
- Ayuda oficial de Google Trends para exportar resultados: <https://support.google.com/trends/answer/4365533>
- `pytrends` en GitHub: <https://github.com/GeneralMills/pytrends>
