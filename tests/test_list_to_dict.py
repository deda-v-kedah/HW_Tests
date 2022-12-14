import pytest
from main import list_to_dict

@pytest.mark.parametrize(
    "i_list, o_dict",
    [([1,2,3], {1:{2:3}}),
     ([1,2,3,4], {1:{2:{3:4}}}),
     ([1,2,3,4,5], {1:{2:{3:{4:5}}}}),
     (['2018-01-01', 'yandex', 'cpc', 100], {'2018-01-01': {'yandex': {'cpc': 100}}})]
)
def test_listtodict(i_list, o_dict):
    res = list_to_dict(i_list)
    assert res == o_dict
