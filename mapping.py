import webbrowser
import pandas as pd

df_skill = pd.read_excel(r'E:\project\public\number\trunk\Z-战斗新表.xlsx', sheet_name='技能总表')
df_general = pd.read_excel(r'E:\project\public\number\trunk\W-武将表.xlsx', sheet_name='武将')
df_pet = pd.read_excel(r'E:\project\public\number\trunk\C-宠物表2.xlsx', sheet_name='幻兽总表')
df_effect = pd.read_excel(r'E:\project\public\number\trunk\Z-战斗新表.xlsx', sheet_name='效果总表')
# # 将 DataFrame 转换为 HTML 文件
# skill_path = "skill.html"
# df_skill.to_html(skill_path)

# # 在默认浏览器中打开
# webbrowser.open(skill_path)

# 将 '技能唯一id' 和 '技能名' 映射为字典
skill_mapping = df_skill.iloc[3:,1:3].set_index('技能唯一id')['技能名'].to_dict()
# 将 '武将唯一id' 和 '武将名' 映射为字典
general_mapping = df_general.iloc[3:,1:3].set_index('武将ID')['名字'].to_dict()
# 将 '幻兽唯一id' 和 '幻兽名' 映射为字典
pet_mapping = df_pet.iloc[3:,1:3].set_index('唯一ID（从1开始)')['宠物名称'].to_dict()
# 将 '效果唯一id' 和 '效果名' 映射为字典
effect_mapping = df_effect.iloc[3:,1:3].set_index('唯一标识')['描述'].to_dict()


if __name__ == "__main__":

    print(skill_mapping)

    print(general_mapping)
    
    print(pet_mapping)

    print(effect_mapping)

