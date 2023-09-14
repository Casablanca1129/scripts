#!/bin/bash
# 脚本名称: scan.sh
# 作者: azheng
# 版本: 1.0
# 日期: 2023-09-14
# 描述: 在指定IP上执行masscan和nmap端口扫描

# 设置全局变量
declare -a ports=()  # 用于存储扫描到的端口

# 提示用户输入IP地址
read -p "请输入IP地址 (默认为 10.10.10.10): " ip
ip=${ip:-"10.10.10.10"}  # 如果用户未输入，默认为 10.10.10.248

# 提示用户输入线程数
read -p "请输入线程数 (默认为 5000): " threads
threads=${threads:-5000}  # 如果用户未输入，默认为 5000

# 函数定义 - 执行masscan端口扫描并获取端口列表
function masscan_ports {
  sudo masscan -p- $ip --rate $threads -e tun0 | grep 'open' | awk -F ' ' '{print $4}' | awk -F '/' '{print $1}' | sort -n | uniq -u > masscan_ports
  mapfile -t ports < masscan_ports  # 将端口列表读入数组
}

# 函数定义 - 执行nmap端口扫描并获取端口列表
function nmap_ports {
  nmap -p- $ip --min-rate $threads -T4 | grep 'open' | awk -F '/' '{print $1}' | sort -n | uniq -u > nmap_ports
  mapfile -t ports < nmap_ports  # 将端口列表读入数组
}

# 主程序
function main {
  echo "执行masscan端口扫描..."
  masscan_ports
  echo "执行nmap端口扫描..."
  nmap_ports

  # 输出扫描到的端口
  # 去重和排序
  sorted_ports=($(printf "%s\n" "${ports[@]}" | sort -n | uniq))
  echo "扫描到的端口: ${sorted_ports[@]}"

  
  # 将端口数组转换成逗号分隔的字符串
  port_str=$(IFS=,; echo "${ports[*]}")
  
  # 执行最终的nmap扫描
  echo "执行nmap扫描..."
  nmap -sTVC -p$port_str $ip --min-rate $threads -T4 -Pn
}

# 脚本入口
main

