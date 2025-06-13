from pprint import pprint
import pandas  as pd
import webbrowser
import json
import os

# 获取当前脚本所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建 config.json 路径
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'neighbor_config.json')
def web_open(df,html_path):
    # 将 DataFrame 转换为 HTML 文件
    html_path = html_path
    df.to_html(html_path)
    webbrowser.open(html_path)

def check_neighbor_city_config(neighbor_config):
    city_config = pd.read_excel(neighbor_config['path'],sheet_name=neighbor_config["sheet"])

    neighbor_tuple_list = city_config[[neighbor_config['colA'], neighbor_config['colB']]][3:].apply(lambda row: (str(row[neighbor_config["colA"]]), row[neighbor_config["colB"]].split(',')), axis=1).to_list()
    neighbor_dict = {i[0]: i[1] for i in neighbor_tuple_list}
    # pprint(neighbor_dict)

    for key in neighbor_dict:
        for value in neighbor_dict[key]:
            if key not in neighbor_dict[value]:
                print(f"错误: {key} 的相邻{neighbor_config["type"]} {value} 的相邻{neighbor_config["type"]} 列表中不存在{key}")

if __name__ == "__main__":
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        neighbor_config = json.load(f)['configs']
    for config in neighbor_config:
        check_neighbor_city_config(config)
        print("\n")

    print("检查完成，结果已输出。")