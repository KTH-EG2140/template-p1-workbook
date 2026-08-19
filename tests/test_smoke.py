"""Smoke test: the package is installed and importable. Ships passing."""
import svedala_toolbox


def test_package_imports():
    assert svedala_toolbox.__version__
