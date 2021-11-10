import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from learning import app01, app04, app05, app06, app07
from invoker.invoker import invoker
from wechat import models
from wechat.database import engine

# 建表，存在会忽略
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API文档",
    description="这是API文档描述",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redocs"

)

# app.include_router(app01, prefix="/chaper01", tags=["参数校验"])
# app.include_router(app04, prefix="/chaper04", tags=["请求响应"])
# app.include_router(app05, prefix="/chaper05", tags=["依赖"])
# app.include_router(app06, prefix="/chaper06", tags=["授权模式"])
# app.include_router(app07, prefix="/chaper07", tags=["DB操作"])
app.include_router(invoker, prefix="/invoker", tags=["服务器校验"])


if __name__ == '__main__':
    uvicorn.run('run:app', host="0.0.0.0", port=8000, reload=True, debug=True, workers=1)
