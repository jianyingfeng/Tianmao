import pytest
from TUGithubAPI.onlinebusiness import OnlineBusiness
from TUGithubAPI.operations.login import login_success

@pytest.fixture(autouse=True,scope='module')
def ob():
    api_root_url = 'http://127.0.0.1'
    onlinebusiness = OnlineBusiness(api_root_url)
    ###必须是.ob，因为login_success返回的是result，而不是result.ob
    yield login_success(onlinebusiness,'phone','pwd').ob