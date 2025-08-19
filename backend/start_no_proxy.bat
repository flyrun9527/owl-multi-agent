@echo off
REM 清除代理环境变量
set HTTP_PROXY=
set HTTPS_PROXY=
set http_proxy=
set https_proxy=
set ALL_PROXY=
set all_proxy=
set NO_PROXY=localhost,127.0.0.1,::1
set no_proxy=localhost,127.0.0.1,::1

REM 启动后端服务
echo Starting backend without proxy...
uv run uvicorn main:api --port 15001
