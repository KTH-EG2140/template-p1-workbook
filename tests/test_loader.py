"""Tests for the Svedala loader.

One test is written for you as a model. Lab 1 ends with you writing THE
FIRST TEST THE SVEDALA LOADER HAS EVER HAD — one more test, yours, that
checks something you think matters. Ideas: the slack generator is the
one flagged in generators.csv, all loads sit on existing buses, total
load is what you expect, a 400 kV line got the 2.0 kA limit. Tip: test
VALUES, not just "column is filled" — a test that passes when every
limit is 999 kA proves nothing.
"""
import pandapower as pp
import pytest

from svedala_toolbox.loader import load_svedala, run_power_flow


def test_network_sizes():
    """The model has the element counts we know from the data."""
    net = load_svedala()
    # One assertion message as a model: without it, a failure just says "52 != 51".
    assert len(net.bus) == 52, f"expected 52 buses, got {len(net.bus)} — check index_col=0"
    assert len(net.line) == 52
    assert len(net.trafo) == 44
    assert len(net.gen) == 36
    assert len(net.load) == 60


def test_power_flow_converges():
    """The base case solves."""
    net = run_power_flow(load_svedala())
    assert net.converged


# TODO (Lab 1): your test goes here.
