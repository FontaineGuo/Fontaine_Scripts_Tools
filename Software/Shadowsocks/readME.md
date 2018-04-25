# shadowsocks for centOS一键脚本
- [启动脚本](#启动脚本)
- [单端口设置](#单端口设置)
- [多端口设置](#多端口设置) 
- [常用设置](#常用设置)


## 启动脚本
#### 该脚本适用于CentOS 7 x64
先在服务器上安装git
```
yum install git
```
之后键入
```
wget https://raw.githubusercontent.com/FontaineGuo/FontaineLinuxScripts/master/Software/Shadowsocks/Shadowsocks_CentOS.sh
```
此时会要求输入加密方式
```
"请输入加密方式 (推荐aes-256-cfb)"
```
建议使用aes-256-cfb,
之后会要求输入用户端口数，倘若是自用，只需输入一1即可，多端口则输入所需端口数
```
"1：输入你想创建的端口数量"
```
之后单用户和多用户将会有不同的设置方式

## 单端口设置
出现如下提示，按照样例进行输入即可
#### 样例
```
请输入服务器端口:
500
请输入密码:
password
```
等待脚本进行自动设置，出现
```
配置完成
```
时，此时ss脚本已经在后台启动

## 多端口设置
假设有3个端口，脚本会要求输入三次3个端口与密码
#### 样例
```
——————————请输入第1个端口号——————————
500
——————————请输入第1个端口的密码——————————
password
第1个端口号500，密码为：password(此行为提示，不需要键入)
——————————请输入第2个端口号——————————
501
——————————请输入第2个端口的密码——————————
password
第2个端口号501，密码为：password(此行为提示，不需要键入)
——————————请输入第3个端口号——————————
502
——————————请输入第3个端口的密码——————————
password
第3个端口号500，密码为：password(此行为提示，不需要键入)
```
等待脚本进行自动设置，出现
```
配置完成
```
时，ss脚本已经在后台启动


## 常用设置
#### 后台启动
```
nohup ssserver -c /etc/shadowsocks.json &
```
#### 停止服务
```
ssserver -d stop
```
#### 卸载ss
```
yum uninstall shadowsocks
```