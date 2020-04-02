import pytest

from oxide import create_app


@pytest.mark.unit
@pytest.mark.compile
def test_config():
    """Test create_app without passing test config."""
    with pytest.raises(RuntimeError):
        create_app()
