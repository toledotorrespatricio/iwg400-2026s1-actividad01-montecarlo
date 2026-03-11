"""Descarga datos de Google Trends y los guarda como CSV.

Este script usa ``pytrends``, una libreria no oficial. El objetivo es dejar un
flujo reproducible para la clase, no depender de un CSV inventado.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from pytrends.request import TrendReq


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Descargar datos de Google Trends y guardarlos en CSV.",
    )
    parser.add_argument(
        "--keywords",
        nargs="+",
        required=True,
        help="Lista de terminos a comparar, por ejemplo: ChatGPT TikTok Instagram",
    )
    parser.add_argument(
        "--geo",
        default="CL",
        help="Codigo geografico de Google Trends. Ejemplo: CL para Chile.",
    )
    parser.add_argument(
        "--timeframe",
        default="today 3-m",
        help='Ventana temporal. Ejemplo: "today 3-m" o "today 12-m".',
    )
    parser.add_argument(
        "--output",
        default="data/google_trends.csv",
        help="Ruta de salida del CSV.",
    )
    parser.add_argument(
        "--hl",
        default="es-CL",
        help="Idioma de la sesion de Trends.",
    )
    parser.add_argument(
        "--tz",
        type=int,
        default=180,
        help="Zona horaria en minutos. Chile continental suele usar 180.",
    )
    return parser


def download_trends(keywords: list[str], geo: str, timeframe: str, hl: str, tz: int) -> pd.DataFrame:
    # Abrimos una sesion de pytrends. La libreria se encarga de hablar con Google Trends.
    pytrends = TrendReq(hl=hl, tz=tz)

    # Esta linea prepara la consulta: terminos, pais y ventana temporal.
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop="")

    # Google Trends devuelve una tabla indexada por fecha.
    df = pytrends.interest_over_time()
    if df.empty:
        raise RuntimeError("Google Trends devolvio una tabla vacia. Prueba con otro rango o terminos.")

    # La columna isPartial aparece a veces; no es necesaria para la actividad.
    if "isPartial" in df.columns:
        df = df.drop(columns=["isPartial"])

    # Dejamos la fecha como columna normal para trabajar mas facil en notebooks.
    df = df.reset_index()
    return df


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    df = download_trends(
        keywords=args.keywords,
        geo=args.geo,
        timeframe=args.timeframe,
        hl=args.hl,
        tz=args.tz,
    )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)

    print(f"Archivo guardado en: {output}")
    print("Columnas:", ", ".join(df.columns))
    print(f"Filas descargadas: {len(df)}")


if __name__ == "__main__":
    main()
