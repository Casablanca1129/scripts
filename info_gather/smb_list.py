import subprocess
import re
import os
# 获取 SMB 服务器的 IP 地址
# smb_server_ip = input("Enter SMB server IP address: ")
smb_server_ip = '10.10.10.103'
# 运行 smbclient 命令并将输出存储到变量中
command = f"smbclient -N -L \\\\{smb_server_ip}"
output = subprocess.check_output(
    command, shell=True, stderr=subprocess.DEVNULL).decode("utf-8")

share_names = re.findall(r'^\s*(.*)\s*Disk.*', output, re.MULTILINE)


# 解析输出并获取共享列表
for share in share_names:
    share = share.strip()
    command = f"smbclient -N \"//{smb_server_ip}/{share}\" -c dir"
 #  share_output = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL).decode("utf-8")
    share_output = os.popen(command).read()
    print(share+':')
    print(share_output)

# list=list()
#depth=0
#def listpath (lastpath,depth)
# 	command (dir lastpath)
# 	getdirct = out grep "D" #list
# 	getfile = out grep "f" 
#	print([x for x in getfile]+" f")
#
#	if getdirct == [".",".."]
#		print(lastpath)
#	else
#		depth=depth+4
#    		for dname in getdirct
#			listpath(lastpath+dname,depth)
