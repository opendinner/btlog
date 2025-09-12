
import webbrowser
import pandas as pd


dict_attacker = {
                "1": 2570,
                "2": 160750,
                "3": 0,
                "4": 0,
                "5": 2000,
                "6": 0,
                "7": 0,
                "8": 15,
                "9": 240,
                "10": 0,
                "11": 0,
                "12": 0,
                "13": 360,
                "14": 120,
                "15": 60,
                "16": 60,
                "17": 120,
                "18": 180,
                "19": 30,
                "20": 0,
                "21": 0,
                "22": 10000,
                "23": 20,
                "24": 0,
                "25": 0,
                "26": 0,
                "27": 300,
                "28": 160750
            }

dict_defender = {
                "1": 198,
                "2": 2158,
                "3": 0,
                "4": 0,
                "5": 2000,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
                "10": 0,
                "11": 0,
                "12": 0,
                "13": 0,
                "14": 0,
                "15": 0,
                "16": 0,
                "17": 0,
                "18": 0,
                "19": 0,
                "20": 0,
                "21": 0,
                "22": 10000,
                "23": 20,
                "24": 0,
                "25": 0,
                "26": 0,
                "27": 0,
                "28": 2158
            }

df1 = pd.DataFrame.from_dict(dict_attacker, orient='index', columns=['value'])
df2 = pd.DataFrame.from_dict(dict_defender, orient='index', columns=['value']) 
df_combined = pd.concat([df1, df2], axis=1).to_csv("attrs.csv")

webbrowser.open( "attrs.csv")
print("csv文件已生成并在浏览器中打开。") 