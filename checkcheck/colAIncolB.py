import pandas as pd
import json
import os
from pprint import pprint
# 获取当前脚本所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建 config.json 路径
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'AinB_config.json')
def tbl_check(config):

    table_A = config['table_A']
    table_B = config['table_B']
    A_sheet = config['A_sheet']
    B_sheet = config['B_sheet']
    A_col = config['A_col']
    B_col = config['B_col']
    A_index = config['A_index']

    a = pd.read_excel(f'E:\\project\\public\\number\\trunk\\{table_A}.xlsx',sheet_name = A_sheet)

    b = pd.read_excel(f'E:\\project\\public\\number\\trunk\\{table_B}.xlsx',sheet_name = B_sheet)

    not_exist = []
    not_exist_set = set()
    # 使用 itertuples() 方法来迭代 DataFrame 的行
    a1 = a[:][3:]
    for index,row in a1.iterrows():
        # pprint(row)
        cid = row[A_index]
        rid = row[A_col]
        if pd.notna(rid):
            if rid not in b[B_col].values:
                not_exist.append((cid,rid))
                not_exist_set.add(rid)

    for cid,rid in not_exist:
        print(f'{table_A} {A_index} {cid} 所配的 {A_col} {rid} 在 {table_B} 的 {B_col} 中不存在')
    if len(not_exist_set) > 0:
        print(f'\n{table_A}的{A_col} 中 {sorted(not_exist_set)} 不存在\n')
    else:
        print(f'\n{table_A}的{A_col} 中不存在不匹配的值\n')

if __name__ == '__main__':
    # 读取配置文件
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        configs = json.load(f)

    # 批量执行检查
    for config in configs:
        tbl_check(configs[config])