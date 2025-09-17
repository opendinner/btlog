import re
#复制后端总属性到str
str = 'att=822097,hpMax=16558526,attTime=1000,attPercent=2184,hpMaxPercent=2807,critRate=5310,evade=5310,freeze=7020,suck=3600,critRateDef=15660,evadeDef=15660,freezeDef=15660,suckDef=15660,damEnhance=1175,damAbsorb=800,cureAdd=660,cureReduce=540,skillAdd=2923,bbAdd=1020,bbReduce=1500,jiangAdd=580,jiangReduce=2311,attSpeedRate=10000,strategyRecover=20,attDamEnhanceAtFight=2880,attDam=10000,attDamReduceAtFight=4467'
lt1 = str.split(',')
#复制前端总属性object到str2（json格式）
str2 = {
    "att": 822097,
    "hpMax": 16558526,
    "attTime": 1000,
    "attDam": 10000,
    "attPercent": 2184,
    "hpMaxPercent": 2807,
    "critRate": 5310,
    "evade": 5310,
    "freeze": 7020,
    "suck": 3600,
    "critRateDef": 15660,
    "evadeDef": 15660,
    "freezeDef": 15660,
    "suckDef": 15660,
    "damEnhance": 1175,
    "damAbsorb": 800,
    "cureAdd": 660,
    "cureReduce": 540,
    "critDegree": 0,
    "critDegreeDef": 0,
    "skillAdd": 2923,
    "skillReduce": 0,
    "bbAdd": 1020,
    "bbReduce": 1500,
    "jiangAdd": 580,
    "jiangReduce": 2311,
    "shenqiAdd": 0,
    "shenqiReduce": 0,
    "strategyInitial": 0,
    "attSpeedRate": 10000,
    "strategyRecover": 20,
    "attDamEnhanceAtFight": 2880,
    "attDamReduceAtFight": 4467,
    "hpMaxPercentAtFight": 0,
    "attDamEnhanceFinal": 0,
    "attDamDefenceFinal": 0,
    "attDamPercent": 0,
    "jiangSkillFightEnhance": 0
}
lt2 = []
for key in str2:
    lt2.append(f'{key}={str2[key]}')

diff = 0
for i in range(len(lt1)):
    if lt1[i] not in lt2:
        print(lt1[i])
        diff+=1
print(f"{diff}个属性不一样")

