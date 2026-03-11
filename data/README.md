# Data

Esta carpeta guarda archivos generados durante la actividad.

Archivo esperado:

- `google_trends.csv`: serie temporal descargada desde Google Trends.

No se incluye un CSV dummy. La idea es generar este archivo con:

```bash
python scripts/fetch_google_trends.py --keywords ChatGPT TikTok Instagram --geo CL --timeframe "today 3-m"
```

Si la descarga automatica falla, puedes exportar manualmente desde Google Trends y guardar el archivo con ese nombre.
