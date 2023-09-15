import io
import PyPDF2
import requests
import threading

keywords = ['user', 'password', 'account', 'intelligence', 'htb', 'login', 'service', 'new']
users = set()

# 用于处理单个 URL 的函数
def process_url(url):
    resp = requests.get(url.strip())  # 去除 URL 两端的空白字符

    # 检查响应状态码是否为 200（HTTP 成功状态码）
    if resp.status_code == 200:
        # 使用 io.BytesIO 创建一个字节流对象，并将响应内容写入其中
        with io.BytesIO(resp.content) as data:
            # 创建一个 PdfFileReader 对象来处理 PDF 文件
            pdf = PyPDF2.PdfFileReader(data)

            # 提取 PDF 文件的创建者信息，并将其添加到用户集合中
            users.add(pdf.getDocumentInfo().get('/Creator', 'Unknown'))

            # 遍历 PDF 文件的所有页面
            for page in range(pdf.getNumPages()):
                # 提取页面文本
                text = pdf.getPage(page).extractText()

                # 检查文本是否包含任何关键词
                if any([k in text.lower() for k in keywords]):
                    # 如果包含关键词，打印 PDF 文件的 URL 和相关文本
                    print(f'==={url}===\n{text}')

# 打开文件以供读取
with open('pdflist', 'r') as file:
    threads = []

    while True:
        url = file.readline()
        if not url:
            break  # 如果读取的 URL 为空，表示到达文件末尾，退出循环

        # 创建线程来处理单个 URL
        thread = threading.Thread(target=process_url, args=(url,))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

# 将用户集合中的内容写入文件
with open('users', 'w') as f:
    f.write('\n'.join(users))

