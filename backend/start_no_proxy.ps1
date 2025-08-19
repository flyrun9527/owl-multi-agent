# 清除代理环境变量
$env:HTTP_PROXY = ""
$env:HTTPS_PROXY = ""
$env:http_proxy = ""
$env:https_proxy = ""
$env:ALL_PROXY = ""
$env:all_proxy = ""
$env:NO_PROXY = "localhost,127.0.0.1,::1"
$env:no_proxy = "localhost,127.0.0.1,::1"

# 显示当前代理设置
Write-Host "Current proxy settings cleared:"
Write-Host "HTTP_PROXY: $env:HTTP_PROXY"
Write-Host "HTTPS_PROXY: $env:HTTPS_PROXY"
Write-Host "NO_PROXY: $env:NO_PROXY"

# 启动后端服务
Write-Host "Starting backend without proxy..."
uv run uvicorn main:api --port 15001
