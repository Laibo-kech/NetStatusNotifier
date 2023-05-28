# Developer：shiwenxiang
# Time:2023/4/1 15:16
import requests
import time
import subprocess

# 设置超时时间
timeout = 5

# 要访问的 URL
url = 'https://www.google.com'

# 尝试访问 URL
try:
    response = requests.get(url, timeout=timeout)
    # 如果响应码为 200，则表示可以访问
    if response.status_code == 200:
        # 显示提示窗口
        subprocess.call(['osascript', '-e', 'display notification "国际通用网络" with title "当前网络状态"'])
    else:
        # 显示国内局域网络
        subprocess.call(['osascript', '-e', 'display notification "国内局域网络" with title "当前网络状态"'])
# 如果访问超时或出错，则表示无法访问
except:
    # 显示国内局域网络
    subprocess.call(['osascript', '-e', 'display notification "国内局域网络" with title "当前网络状态"'])
