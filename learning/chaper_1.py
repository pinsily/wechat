from enum import Enum
from typing import List, Optional

from fastapi import APIRouter, Path, Query, Cookie, Header
from pydantic import BaseModel, Field

app01 = APIRouter()


# 函数的顺序就是匹配路由的顺序

@app01.get("/")
def hello():
    """
    示例
    :return:
    """
    return {"hello": "chaper01"}


# 枚举类
class CityName(str, Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"


@app01.get("/enum/{city}")
def enum_learn(city: CityName):
    if city == CityName.Beijing:
        return {"city": CityName.Beijing}
    if city == CityName.Shanghai:
        return {"city": CityName.Shanghai}
    return {"city": "none"}


# 文件路径参数 如果有 / 符号的话当成参数
@app01.get("/files/{file_path:path}")
def filepath(file_path: str):
    return {"filepath": file_path}


# 参数校验
@app01.get('/valid_num/{num}')
def valid_num(
        num: int = Path(..., title="数字", description="不可描述的数字", ge=1, le=10)
):
    return num


# 查询参数的校验
@app01.get('/validations')
def query_params_validate(
        value: str = Query(..., min_length=8, max_length=16, regex="^a"),
        values: List[str] = Query(default=['v1', 'v2'], alias="别名")
):
    return value, values


# 布尔类型可以很多转换：yes\Yes\1之类的


"""请求体和Fields"""


class CityInfo(BaseModel):
    name: str = Field(..., example="Beijing")
    country: str
    country_code: str = None
    population: int = Field(default=8000, title="人口数量", description="国家的人口数量")

    class Config:
        schema_extra = {
            # 示例
            "example": {
                "name": "Shanghai",
                "country": "china",
                "country_code": "CN",
                "population": 140000000
            }
        }


@app01.post("/requests_body/city")
def city_info(city: CityInfo):
    print(city.name, city.country)
    return city.dict()


# 混合参数

@app01.put('/requests_body/city/{name}', tags=["混合参数"])
def mix_city_info(
        name: str,  # 链接变量
        city01: CityInfo,  # 请求体
        city02: CityInfo,
        confirmed: int = Query(default=0, description="确诊数", ge=0),  # 链接请求参数
        death: int = Query(default=0, description="死亡数", ge=0)
):
    if name == "Shanghai":
        return {"Shanghai": {"confirmed": confirmed, "death": death}}
    return city01.dict(), city02.dict()


"""Cookies和Headers"""


@app01.get("/cookie")
def cookie(cookie_id: Optional[str] = Cookie(None)):
    return {"cookie_id": cookie_id}


@app01.get("header")
def header(user_agent: Optional[str] = Header(None, convert_underscores=True), x_token: List[str] = None):
    return {"User-Agent": user_agent, "x_token": x_token}
