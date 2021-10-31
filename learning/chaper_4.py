from typing import Optional, Union, List

from fastapi import APIRouter, Form, File, UploadFile
from pydantic import BaseModel
from starlette import status

app04 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


user_list = {
    "pinsily": {"username": "pinsilyzhu", "mobile": "10000", "address": "广东省", "full_name": "pinsily"}
}


@app04.post('/response_model', response_model=UserOut, response_model_exclude_unset=True)
async def get_model(user: UserIn):
    """
    response_model_exclude_unset=True 返回值不包含默认值
    :return:
    """
    print(user.username)
    return user_list["pinsily"]


# 返回值包含和排除字段
@app04.post("/response_model_attributes",
            response_model=Union[UserIn, UserOut],
            response_model_include=["username", "mobile"])
async def response_model_attributes(user: UserIn):
    return user


"""状态码"""


@app04.post("/status_code", status_code=status.HTTP_200_OK)
async def status_code():
    return {"status_code", status.HTTP_200_OK}


"""表单数据"""


@app04.post("/login")
async def login(username: str = Form(..., regex="^p"), password: str = Form(...)):
    """
    pip install python-multipart 表单元数据的处理
    :param username:
    :param password:
    :return:
    """
    print(password)
    return {"username": username}


"""文件上传"""


@app04.post("/upload_file")
def upload_file(file: bytes = File(...)):
    """
    File类：bytes形式读入内存，适合小文件
    多个文件使用 List[bytes]
    :param file:
    :return:
    """
    return {"file_size": len(file)}


@app04.post("/upload_files")
def upload_files(files: List[UploadFile] = File(...)):
    """
    文件内存中达到阈值会先部分存入磁盘
    适合用于大文件
    上传的对象为python文件对象，可以直接操作
    :param files:
    :return:
    """
    filename_list = list()
    for file in files:
        filename_list.append(file.filename)
    return {"filename_list": filename_list}


"""路径操作配置"""


@app04.post(
    "path_operation_configuration",
    response_model=UserOut,
    tags=['路径参数'],
    summary="This is summary",
    description="This is summary",
    response_description="This is respnse descript",
    # deprecated=True
    status_code=status.HTTP_200_OK
)
async def path_operation_config(user: UserIn):
    """

    :param user:
    :return:
    """
    return user.dict()