import pytest

def test_modifyUserNick(ob):
    payload = {"nickName":"鸡腿"}
    response = ob.user.modifyUserNick(json=payload)
    assert response.content['status'] == '0000'