# django-starter-kit

django starter kit for django 1.10 LTS


## Features


#### 常用命令封装

使用 Makefile

支持命令行自动补全参数


#### 日志功能完善

debug 时的 console log, 包含请求时间。

ERROR 级的错误，自动上报至Rollbar. https://rollbar.com/
可在 rollbar 中配置短信／邮件提醒。
方便运维／bug 修复。


#### Admin 系统

皮肤使用 grappelli


#### 安全／干净的 settings.py

从环境变量中读取关键的配置参数

方便与 ansible / docker 等的集成部署
