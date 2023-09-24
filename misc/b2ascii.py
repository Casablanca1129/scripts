import sys

if len(sys.argv) != 2:
    print("用法: python script.py 二进制字符串")
    sys.exit(1)

binary_data = sys.argv[1]  # 获取命令行参数中的二进制字符串
ascii_text = ''

# 将连续的8位二进制分组转换为ASCII字符
for i in range(0, len(binary_data), 8):
    binary_chunk = binary_data[i:i + 8]
    decimal_value = int(binary_chunk, 2)
    ascii_text += chr(decimal_value)

print("转换后的ASCII文本为:", ascii_text)

