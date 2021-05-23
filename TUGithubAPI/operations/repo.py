from TUGithubAPI.api.repositories.repos import Repos
from TUGithubAPI.core.base import CommonItem

###编写这个函数的目的是为了将github提供的创建私人仓库和组织仓库的接口封装成一个接口
def create_repo(github,name,org=None,description=None, homepage=None, private=False, has_issues=True,
                has_projects=True, has_wiki=True,auto_init=True):
    ###auto_init=True，必须,否则代码仓不会创建原始分支
    result = CommonItem()
    payload = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init
    }

    result.success = False
    if org:
        response = github.repos.create_org_repo(org=org,json=payload)
    else:
        response = github.repos.create_user_repo(json=payload)
    result.response = response
    if response.status_code == 201:
        result.success = True
    else:
        result.error = 'create repo got {},should be 201'
    return result

def create_branch(github,owner,repo,new_branch_name,source_branch_name):
    result = CommonItem()
    result.success = True
    result.error = None
    response = github.gitdata.refs.get_a_reference(owner,repo,source_branch_name)
    if response.status_code !=200:
        result.success = False
        result.error = 'got source branch sha fails,repo={} got {},should be 200'.format(repo,response.status_code)
        result.response = response
        return result       ###代码走到这就不会往下走了
    source_branch_sha = response.content['object']['sha']
    pay_load = {
    "ref": "refs/heads/{}".format(new_branch_name),
    "sha": source_branch_sha
}
    response = github.gitdata.refs.create_a_reference(owner,repo,json=pay_load)
    if response.status_code != 201:
        result.success = False
        result.error = 'create branch fails,repo={} got {},should be 201'.format(repo, response.status_code)
        result.response = response
        return result
    result.response=response
    return result          ###一定要返回result