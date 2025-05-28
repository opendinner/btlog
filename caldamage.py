import math
import numpy as np

def calroledamage(att,skillRatio,dam_enhance,dam_absorb,roleenhance,rolereduce,roledegree = 0):

    damage = np.floor((att * skillRatio/10000) * np.maximum((1+(dam_enhance - dam_absorb)/10000),0.1) * (1+(roleenhance - rolereduce)/10000)* (1 + roledegree/10000))
    return damage
def caljiangdamage(att,skillRatio,dam_enhance,dam_absorb,jiangenhance,jiangreduce,jiangdegree = 0):
    damage = np.floor((att * skillRatio/10000) * np.maximum((1+(dam_enhance - dam_absorb)/10000),0.1) * (1+(jiangenhance - jiangreduce)/10000)* (1 + jiangdegree/10000))
    return damage
att = np.floor(5526*(1+(3176+5000)/10000))

print(calroledamage(att,10000,0,100100,1200,400))

