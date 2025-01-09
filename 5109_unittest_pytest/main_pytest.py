from reverse import reverse
import pytest

def test_reverse():
    assert reverse('asdf') == "fdsa"

def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(1501)
