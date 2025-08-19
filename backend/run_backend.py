#!/usr/bin/env python3
"""
Backend启动脚本 - 绕过代理设置
"""
import os
import sys
import subprocess
from pathlib import Path

def clear_proxy_env():
    """清除代理环境变量"""
    proxy_vars = [
        'HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy',
        'ALL_PROXY', 'all_proxy', 'FTP_PROXY', 'ftp_proxy',
        'SOCKS_PROXY', 'socks_proxy'
    ]
    
    for var in proxy_vars:
        if var in os.environ:
            del os.environ[var]
            print(f"Cleared {var}")
    
    # 设置NO_PROXY
    os.environ['NO_PROXY'] = 'localhost,127.0.0.1,::1,*.local'
    os.environ['no_proxy'] = 'localhost,127.0.0.1,::1,*.local'
    print("Set NO_PROXY variables")

def main():
    """主函数"""
    print("=" * 50)
    print("启动Backend服务 (无代理模式)")
    print("=" * 50)
    
    # 清除代理设置
    clear_proxy_env()
    
    # 设置Python编码
    os.environ["PYTHONIOENCODING"] = "utf-8"
    
    # 切换到脚本所在目录
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print(f"工作目录: {os.getcwd()}")
    print("启动命令: uv run uvicorn main:api --port 15001")
    print("-" * 50)
    
    try:
        # 启动服务
        subprocess.run([
            "uv", "run", "uvicorn", "main:api", 
            "--port", "15001",
            "--host", "0.0.0.0"
        ], check=True)
    except KeyboardInterrupt:
        print("\n服务已停止")
    except subprocess.CalledProcessError as e:
        print(f"启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
