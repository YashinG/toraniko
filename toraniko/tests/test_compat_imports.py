"""Tests for backward-compatible import aliases."""

from torikano.model import _factor_returns, estimate_factor_returns


def test_torikano_model_alias_exports_symbols():
    assert callable(_factor_returns)
    assert callable(estimate_factor_returns)
