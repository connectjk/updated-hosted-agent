"""Smoke tests for Updated-Hosted-agent."""


def test_imports():
    """Verify main module can be imported."""
    import main  # noqa: F401


def test_instructions():
    """Verify instructions are defined."""
    import main
    assert len(main.INSTRUCTIONS) > 0
