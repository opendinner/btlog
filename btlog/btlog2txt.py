import json
import pandas as pd
import webbrowser
import log_parser
import sys
import os

output_time = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')

s_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(s_path,'btlog.json')
output_file = os.path.join(s_path,f'console_output_{output_time}.txt')
def web_open(df,html_path = "output.html"):
    # 将 DataFrame 转换为 HTML 文件
    html_path = html_path
    df.to_html(html_path)
    webbrowser.open(html_path)
    
if __name__ == '__main__':    
    # 重定向标准输出到文件
    with open(output_file, 'w', encoding='utf-8') as g:
        # 保存原来的stdout
        original_stdout = sys.stdout
        # 将stdout重定向到文件
        sys.stdout = g

        # 读取 JSON 文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            resource = json.load(f)

        log = []

        for i in resource['actions']:
            log.append([i['timestamp'], i])

        for i in resource['buffs']:
            log.append([i['timestamp'], i])

        for i in resource['states']:
            log.append([i['timestamp'], i])

        log.sort(key=lambda x: x[0])

        # df = pd.DataFrame(log, columns=['timestamp', 'data'])
        # web_open(df)

        for i in log:
            log_parser.parse(i)

        # 恢复原来的stdout
        sys.stdout = original_stdout

    print(f"输出已保存到 console_output_{output_time}.txt")

        # 在默认浏览器中打开
    webbrowser.open(output_file)