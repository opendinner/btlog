import pandas as pd
import json

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
    for row in a[:][4:].dropna(subset=[A_col]).itertuples(index=False):

        cid = getattr(row, A_index)
        rid = getattr(row, A_col)
        if  rid:
            if rid not in b[B_col].values:
                not_exist.append((cid,rid))
                not_exist_set.add(rid)

    for cid,rid in not_exist:
        print(f'{table_A} {A_index} {cid} 所配的 {A_col} {rid} 在 {table_B} 的 {B_col} 中不存在')
    
    print(f'\n{A_col} 中 {sorted(not_exist_set)} 不存在')

if __name__ == '__main__':
    # 读取配置文件
    with open('config.json', 'r', encoding='utf-8') as f:
        configs = json.load(f)['configs']

    # 批量执行检查
    for config in configs:
        tbl_check(config)