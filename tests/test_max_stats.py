import pytest
from main import max_stats

def test_max_stat():
    res = max_stats()
    assert res == 'yandex'