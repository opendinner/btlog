import json
import pandas as pd
import webbrowser
import log_parser
import sys
import os
from mapping import attrs_mapping as attrs

output_time = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')

s_path = os.path.dirname(os.path.abspath(__file__))
os.makedirs(s_path + '\\log', exist_ok=True)  # 自动创建不存在的文件夹
input_file = os.path.join(s_path,'btlog.json')
output_file = os.path.join(s_path + '\\log',f'console_output_{output_time}.txt')
output_json = os.path.join(s_path + '\\log',f'console_output_{output_time}.json')

def web_open(df,html_path = "output.html"):
    # 将 DataFrame 转换为 HTML 文件
    html_path = html_path
    df.to_html(html_path)
    webbrowser.open(html_path)
    
def getbattleResult(resource : dict):

    print(resource["attacker"]['master']['name'] + ' vs ' + resource["defender"]['master']['name']+'\n')
    if resource['battleResult'] == 1:
        print("*****挑战失败*****")
    else:
        print("*****挑战成功*****")
    print(f"\n战斗时长{resource['endTime']/1000:.3f}秒\n")

    for i in range(1,len(resource["attacker"]['master']['attrs'])+1):
        # 尝试多种键的类型 (int 和 str)
        key_str = str(i)
        key_int = int(i)
        
        attr_value = resource["attacker"]['master']['attrs'][key_str]
        
        # 检查键是否存在于attrs字典中（先检查str类型，再检查int类型）
        attr_name = None
        if key_str in attrs:
            attr_name = attrs[key_str]
        elif key_int in attrs:
            attr_name = attrs[key_int]
        else:
            # 如果attrs中没有对应的键，使用默认值
            attr_name = f"属性{key_str}"
            
        print(f"{attr_name:<30s}: {attr_value} vs {attr_value}")

    print("\n")



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
        
        #保存json并重命名
        with open(output_json, 'w', encoding='utf-8') as json_file:
            json.dump(resource, json_file, ensure_ascii=False, indent=4)

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
        getbattleResult(resource)

        for i in log:
            log_parser.parse(i)

        # 恢复原来的stdout
        sys.stdout = original_stdout

    print(f"输出已保存到 console_output_{output_time}.txt")

        # 在默认浏览器中打开
    webbrowser.open(output_file)

    '''
    ShieldByLossHpEffectProcessor

            System.out.printf("fighter %d, time %d, sum loss: %d \r\n", target.getMaster().getId(), param.getCurrentTime(), lossHp);
        if (lossHp < lossHpPerTimes) {
            // 先缓存下来先
            passiveSkill.addCacheValue(KEY_LOSS_HP, lossHp);
            return;
        }
        // 次数
        int times = (int) (lossHp / lossHpPerTimes);
        // 剩余的损失值
        lossHp = lossHp % lossHpPerTimes;
        // 缓存剩余的损失值
        passiveSkill.addCacheValue(KEY_LOSS_HP, lossHp);
        System.out.printf("fighter %d add %d * buff, time %d, remaining loss: %d \r\n", target.getMaster().getId(), times, param.getCurrentTime(), lossHp);'''