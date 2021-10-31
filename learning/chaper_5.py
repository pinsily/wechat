from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Header
from starlette import status

app05 = APIRouter()

"""依赖方法的创建和使用"""


async def common_parameters(q: Optional[str] = None, page: int = 1, limit: int = 10):
    return {"q": q, "limit": limit, "page": page}


@app05.get("/dependency")
async def dependency(commons: dict = Depends(common_parameters)):
    return commons


"""类作为依赖"""

fake_item_db = [{"item_name": "Foo"}, {"item_name": "Pinsily"}]


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, page: int = 1, limit: int = 10):
        self.q = q
        self.page = page
        self.limit = limit


@app05.get("/denpendency_class")
async def dependency_class(commons=Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response["q"] = commons.q
    items = fake_item_db[commons.page: commons.page + commons.limit]
    response["items"] = items
    return response


"""子依赖"""


def query(q: Optional[str] = None):
    return q


def sub_query(q: str = Depends(query), last_query: Optional[str] = None):
    if not q:
        return last_query
    return q


@app05.get("/sub_dependency")
async def sub_dependency(final_query: str = Depends(sub_query, use_cache=True)):
    """
    use_cache: 缓存子依赖
    :param final_query:
    :return:
    """
    return {"sub_dependency": final_query}


"""路径操作依赖"""


async def verify_token(x_token: str = Header(...)):
    """无返回值的子依赖"""
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X_token header invalid")
    return x_token


async def verify_key(x_key: str = Header(...)):
    """有返回值的子依赖，但是返回值不会被调用"""
    if x_key != "fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X_key header invalid")
    return x_key


@app05.get("/dependency_in_path", dependencies=[Depends(verify_token), Depends(verify_key)])
async def dependency_in_path():
    """在路径中进行校验"""
    return [{"user": "pinsily"}, {"user": "peng"}]


"""全局依赖"""
# 比如说app05的所有路径都要校验token
# app05 = APIRouter(dependencies=[Depends[verify_token], Depends(verify_key)])


"""yield 子依赖"""

async def get_db():
    db = ""
    try:
        yield db
    finally:
        pass
        # db.close()

