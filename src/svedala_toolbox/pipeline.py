"""Data pipeline: fetch, clean, store. Built in Lab 5.

Follow the LC6/LC7 patterns: cache everything, record provenance,
log every repair, never put a token in source code.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def fetch_load(zone: str, start: str, end: str,
               cache_dir: str | Path = "data_cache") -> pd.Series:
    """Hourly actual load for an ENTSO-E zone, cached with provenance.

    TODO (Lab 5): Parquet cache keyed on (zone, start, end); on miss, fetch via
    entsoe-py and write a JSON provenance sidecar (source, query, retrieved_utc,
    unit). Token from ENTSOE_TOKEN env var or entsoe_token.txt — NEVER hardcoded.
    """
    raise NotImplementedError("Lab 5, task 1")


def clean_load(series: pd.Series) -> tuple[pd.Series, list[str]]:
    """Clean an hourly load series; return (cleaned, repairs_log).

    TODO (Lab 5): UTC index, de-duplicate, remove impossible values,
    interpolate gaps <= 3 h. Every action appends one human sentence to the log.
    Decide and document the long-gap policy.
    """
    raise NotImplementedError("Lab 5, task 2")


def store(series: pd.Series, db_path: str | Path = "svedala.duckdb",
          table: str = "hourly") -> None:
    """Persist to Parquet and register in DuckDB.

    TODO (Lab 5): write Parquet next to db_path; CREATE OR REPLACE the table.
    """
    raise NotImplementedError("Lab 5, task 3")
