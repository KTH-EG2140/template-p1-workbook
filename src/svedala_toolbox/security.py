"""N-1 security classification: dataset building. Built in Lab 8."""
from __future__ import annotations

import pandas as pd


def build_security_dataset(net_loader, year_parquet, n_hours: int = 250,
                           seed: int = 7) -> pd.DataFrame:
    """Sample hours from the year, scale the network, label with YOUR screener.

    Returns a DataFrame: one row per sampled hour, feature columns (zone loads,
    temperatures) + a boolean `insecure` label.

    TODO (Lab 8): zone scaling as in LC9; labelling via your Lab 2 screener.
    Full 52-outage labelling is slow — choose a documented shortcut and state
    in the docstring what it can miss. Commit the resulting table.
    """
    raise NotImplementedError("Lab 8, task 1")
