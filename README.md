# IWG-400: Git, Python y Monte Carlo

Material base para la actividad en clases de IWG-400.

## Que incluye este repositorio

- `docs/actividad01_en_clases_setup_git_notebooks_trends_montecarlo.pdf`: guia de la actividad.
- `notebooks/02_montecarlo_pi.ipynb`: notebook principal de la sesion.
- `requirements.txt`: dependencias minimas del proyecto.
- `data/`: carpeta reservada para actividades futuras con datos.

## Flujo recomendado

1. Clonar el repositorio.
2. Crear y activar un entorno virtual `.venv`.
3. Instalar dependencias con `pip install -r requirements.txt`.
4. Abrir la carpeta completa en VS Code.
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

## Que muestra el notebook

El notebook de Monte Carlo busca aproximar el numero `pi` usando puntos aleatorios en el cuadrado `[-1,1] x [-1,1]`.

La idea matematica es esta:

- el cuadrado tiene area `4`;
- el circulo de radio `1` tiene area `pi`;
- la proporcion de puntos dentro del circulo aproxima `pi/4`;
- por eso `pi ≈ 4 * (puntos dentro / puntos totales)`.

## Publicar en GitHub

Cuando `gh` este autenticado correctamente:

```bash
git add .
git commit -m "feat: actividad inicial de monte carlo"
gh repo create iwg400-actividad01-montecarlo --public --source=. --remote=origin --push
```

## Referencias oficiales

- VS Code: <https://code.visualstudio.com/>
- Python 3.12.10: <https://www.python.org/downloads/release/python-31210/>
- Git: <https://git-scm.com/>
