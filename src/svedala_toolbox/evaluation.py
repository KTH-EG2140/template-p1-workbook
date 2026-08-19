"""Forecast evaluation: persistence and walk-forward. Built in Lab 7, reused in Lab 9."""
from __future__ import annotations

import pandas as pd


def persistence(y: pd.Series, horizon: int = 24) -> pd.Series:
    """The humblest forecaster: value(t) = value(t - horizon).

    TODO (Lab 7): one line — but write the test first.
    """
    raise NotImplementedError("Lab 7, task 1")


def walk_forward(y: pd.Series, model_fn, test_start, test_end,
                 horizon: int = 24) -> pd.DataFrame:
    """Day-by-day out-of-sample evaluation. Never sees the future.

    model_fn(train: pd.Series, horizon: int) -> forecast values for the next
    `horizon` hours. Returns a DataFrame with columns [actual, forecast].
    TODO (Lab 7): loop over test days; extend the training window as days are
    revealed; NEVER refit on data after the day being forecast. Test on a toy series.
    """
    raise NotImplementedError("Lab 7, task 2")
