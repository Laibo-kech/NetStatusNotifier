# NetStatusNotifier

## 项目介绍
NetStatusNotifier是由开发者shiwenxiang在2023年4月1日创建的Python项目，主要用于实时检查网络连接状态并发送通知。如果你在国际网络和国内网络之间切换，这个小工具将是你的得力助手。

## 功能特点
1. 自动检测网络连接状态：可以监测你的机器是否可以访问指定的URL，如Google的主页，以此判断你当前是否接入了国际网络。
2. 系统级别的通知：一旦网络状态发生变化，系统会发送通知，方便你及时了解当前的网络环境。

## 使用指南
1. 首先，你需要克隆这个仓库到你的本地机器上： `git clone https://github.com/shiwenxiang/NetStatusNotifier.git`
2. 然后，进入项目的目录，运行 `net_status_notifier.py` 脚本： `cd NetStatusNotifier` `python net_status_notifier.py`

## 环境依赖
- Python 3.6 或更高版本
- `requests`：Python的HTTP库，用于发送网络请求
- `subprocess`：Python的子进程管理库，用于调用操作系统命令

## 配置指南
在`net_status_notifier.py`脚本中，你可以修改以下配置以适应你的需求：
- `timeout`：网络请求的超时时间，单位是秒
- `url`：需要访问的URL，你可以换成你经常访问的海外网站

## 贡献指南
如果你发现任何问题，或者有新的功能建议，欢迎提交Issue或者Pull Request。

## 许可证
本项目采用MIT许可证，详情请查阅[LICENSE](LICENSE)文件。
