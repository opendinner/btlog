ls_buff = [
        {
            "timestamp": 5049,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 6
                    }
                }
            ]
        },
        {
            "timestamp": 6039,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        },
        {
            "timestamp": 7029,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        },
        {
            "timestamp": 8052,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        },
        {
            "timestamp": 9075,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 6
                    }
                }
            ]
        },
        {
            "timestamp": 10065,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        },
        {
            "timestamp": 11055,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 6
                    }
                }
            ]
        },
        {
            "timestamp": 12045,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        },
        {
            "timestamp": 13068,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 6
                    }
                }
            ]
        },
        {
            "timestamp": 14091,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        },
        {
            "timestamp": 15081,
            "unitId": 1,
            "effect": [
                {
                    "fighterId": 1,
                    "damageMap": {
                        "3": 5
                    }
                }
            ]
        }
    ]


def cal_buff(ls_buff):
    sum = 0
    for i in ls_buff:
        # print(i)
        # print(i["effect"][0]["damageMap"]["3"])
        sum += i["effect"][0]["damageMap"]["3"]

    return sum

def cal_hp_change(ls_action,target):
    sum = 0
    for i in ls_action:
        if "effect"  in i:
            if i["effect"][0]["fighterId"] == target:
                if "damageMap" in i["effect"][0]:
                    if "3" in i["effect"][0]["damageMap"]:
                        sum += i["effect"][0]["damageMap"]["3"]
                    if "1" in i["effect"][0]["damageMap"]:
                        sum -= i["effect"][0]["damageMap"]["1"]
                    if "2" in i["effect"][0]["damageMap"]:
                        sum += i["effect"][0]["damageMap"]["2"]
    return sum



if __name__ == '__main__':
    print(cal_buff(ls_buff))


