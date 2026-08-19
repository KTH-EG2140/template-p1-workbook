"""Lab 7 test skeletons — the harness must be trusted before any model is."""
import pytest


def test_persistence_shifts_exactly():
    pytest.skip("Lab 7: toy series -> persistence(y, 2) equals y shifted by 2")


def test_walk_forward_never_sees_future():
    pytest.skip("Lab 7: model_fn that records its training window; assert no leakage")
