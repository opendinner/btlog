import mapping as m

def parse(data:list):
    if 'skillId' in data[1]:
        parse_action(data)
    elif 'effect' in data[1]:
        parse_buffs(data)    
    if 'effectId' in data[1]:
        parse_state(data)






def parse_buffs(data:list):
    camp = recognize_camp(data)
    for i in data[1]['effect']:
        if 'damageMap' in i.keys():
            print(f" {data[0]} 时 {camp}触发buff {i['damageMap']}",end='，')
            print(f'{i['curHp']}\n')
        if 'attrValues' in i.keys():
            print(f"{data[0]} 时 {camp}buff{i['attrValues']}\n")
        if 'shield' in i.keys():
            print(f"{data[0]} 时 {camp}buff{i['shield']}\n")


def parse_state(data:list):
    camp = recognize_camp(data)

    if data[1]['isAdd'] == 1:
       _swtich = '添加'
    if data[1]['isAdd'] == 0:
        _swtich = '移除'

    print(f" {data[0]} 时 {camp} 的 {data[1]['unitId']} {_swtich} 了效果 {m.effect_mapping[data[1]['effectId']]}({data[1]['effectId']})\n")


def parse_action(data:list):
    camp = recognize_camp(data)

    print(f" {data[0]} 时 {camp} 的 {data[1]['unitId']} 使用 {m.skill_mapping[data[1]['skillId']]}({data[1]['skillId']})",end='，')
    if data[1].get('effect'):
        for i in data[1]['effect']:
            if 'bFreeze' in i and i['bFreeze'] == True:
                    print(f'{i['fighterId']}被定身 ',end='，')
                    
            if 'damageMap' in i:
                if 'bEvade' in i and i['bEvade'] == True:
                    print(f'{i['fighterId']}闪避了攻击 ',end='')
                else:
                    if 'bCritical' in i and i['bCritical'] == True:
                        print(f'对 {i['fighterId']} 造成暴击!!! {i['damageMap']} ',end='，')
                    else:
                        print(f'对 {i['fighterId']} 造成伤害 {i['damageMap']} ',end='，')
            
            if 'recoverMap' in i:
                if 'suckVal' in i:
                    print(f'{i['fighterId']} 吸血回复了 {i['recoverMap']} ',end='，')
                else:
                    if 'bCritical' in i and i['bCritical'] == True:
                        print(f'{i['fighterId']} 血量暴击回复！！！了 {i['recoverMap']} ',end='，')
                    else:
                        print(f'{i['fighterId']} 血量回复了 {i['recoverMap']} ',end='，')
            
            if 'curHp' in i:
                print(f'{i['fighterId']} 当前血量为 {i['curHp']}',end='，')  
            
            if 'maxHp' in i: 
                print(f'{i['fighterId']} 最大血量为 {i['maxHp']}',end='，')

    print('\n')
def recognize_camp(data:list):
    if data[1]['unitId'] < 0:
        camp = '右边'
    elif data[1]['unitId'] > 0:
        camp = '左边'
    return camp