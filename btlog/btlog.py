import json
import pandas as pd
import webbrowser
import log_parser

# 读取 JSON 文件内容
with open('btlog.json', 'r',encoding= 'utf-8') as f:
    resource = json.load(f)

# resource = json.loads('')

log = []

for i in resource['actions']:
    log.append([i['timestamp'],i]) 

for i in resource['states']:
    log.append([i['timestamp'],i])

log.sort(key=lambda x: x[0])

df  = pd.DataFrame(log, columns=['timestamp', 'data'])
# print(df)

# # 将 DataFrame 转换为 HTML 文件
# html_path = "output.html"
# df.to_html(html_path)

# # 在默认浏览器中打开
# webbrowser.open(html_path)

for i in log:
   log_parser.parse(i)

