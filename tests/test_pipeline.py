"""Lab 5 test skeletons — make these pass (token-free: use a committed cache)."""
import pytest

from svedala_toolbox import pipeline


def test_fetch_uses_cache_without_token(tmp_path):
    pytest.skip("Lab 5: commit a small cached sample under tests/data/ and test the cache path")


def test_clean_removes_impossible_values():
    pytest.skip("Lab 5: build a small dirty series by hand; assert negatives/spikes -> repaired + logged")
