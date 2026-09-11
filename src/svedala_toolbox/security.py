"""N-1 security classification: dataset building. Built in Lab 8."""
from __future__ import annotations

import pandas as pd


def build_security_dataset(net_loader, year_parquet, n_hours: int = 250,
                           seed: int = 7) -> pd.DataFrame:
    """Sample hours from the year, scale the network, label with YOUR screener.

    Returns a DataFrame: one row per sampled hour, feature columns (zone loads,
    temperatures) + a boolean `insecure` label.

    TODO (Lab 8): scale each zone's loads by that hour's zone factor AND the
    non-slack generators by the total factor (leave generation at the base case
    and nothing converges); label with the screener's criterion. Full 52-outage
    labelling takes a couple of minutes for 250 hours - a documented shortcut
    (e.g. the 12 severest base-case outages) is optional; state in this
    docstring which policy you chose and what it can miss. `seed` makes the
    hour sample reproducible. Commit the resulting table under tests/data/.
    """
    raise NotImplementedError("Lab 8, task 1")
