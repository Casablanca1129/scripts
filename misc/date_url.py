import datetime
import requests
import threading

# 设置起始日期和结束日期
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2021, 7, 4)

# 定义一个函数，用于下载 PDF 并检查响应状态码
def download_pdf(date):
    url = f"http://10.10.10.248/Documents/{date}-upload.pdf"
    resp = requests.get(url)
    if resp.status_code == 200:
        print(url)

# 创建一个线程池，用于并发下载
threads = []

# 循环生成日期并创建线程
current_date = start_date
while current_date < end_date:
    thread = threading.Thread(target=download_pdf, args=(current_date,))
    thread.start()
    threads.append(thread)
    current_date += datetime.timedelta(days=1)

# 等待所有线程完成
for thread in threads:
    thread.join()

