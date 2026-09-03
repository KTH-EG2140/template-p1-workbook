"""Load the Svedala transmission model into a pandapower network.

Lab 1: port the working code from the L1 warm-up notebook into this module.
The logic already exists — your job is to turn notebook cells into a clean,
importable, testable function. That is an engineering exercise, not a
coding-from-scratch exercise.
"""
from pathlib import Path

import pandas as pd
import pandapower as pp

# Default location of the five Svedala CSV files (bundled with this repo).
DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "svedala"

# Current limits are MISSING in the source data (the max_i_ka column is
# empty). We fill in conservative defaults by voltage level. This is an
# assumption, not a measurement — it returns in Lecturecise 7.
DEFAULT_I_KA = {400.0: 2.0, 220.0: 1.0, 135.0: 0.9}
FALLBACK_I_KA = 0.5


def load_svedala(data_dir: Path = DATA_DIR) -> pp.pandapowerNet:
    """Build the Svedala network from the CSV files in *data_dir*.

    Returns a pandapower network ready for ``pp.runpp``.

    TODO (Lab 1): port the loading code from your L1 warm-up notebook:
      1. read the five CSVs (index_col=0 — the indices matter!)
      2. create an empty network and add buses, lines (fill max_i_ka via
         DEFAULT_I_KA), transformers, generators (keep the slack flag!),
         and loads
      3. return the network
    """
    raise NotImplementedError("Lab 1: port your notebook code here")


def run_power_flow(net: pp.pandapowerNet) -> pp.pandapowerNet:
    """Run an AC power flow and return the solved network.

    TODO (Lab 1): call pp.runpp, and raise a RuntimeError with a helpful
    message if the power flow does not converge (failing loudly beats
    returning nonsense — Lecturecise 3). Watch out: pandapower signals
    non-convergence by RAISING its own pp.LoadflowNotConverged, not by
    returning — catch that and re-raise it as your RuntimeError.
    Second trap: pp.runpp works IN PLACE and returns None — do not
    return its result; return the net you were given.
    """
    raise NotImplementedError("Lab 1")
