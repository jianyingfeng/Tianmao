import pytest
from TUGithubAPI.operations.repo import create_repo,create_branch
from random import randint

def test_create_repo_and_create_a_branch_should_success(env):
    repo_name = "test_repo_{}".format(randint(1,99999))
    result = create_repo(env.github,repo_name)
    assert result.success == True,result.error
    result = create_branch(env.github,'jianyingfeng',repo_name,'jjj','main')
    assert result.success == True,result.error

if __name__ == '__main__':
    pytest.main()