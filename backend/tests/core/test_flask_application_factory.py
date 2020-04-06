import pytest

from oxide import create_app


def test_config():
    """Test create_app without passing test config."""
    with pytest.raises(RuntimeError):
        create_app()
