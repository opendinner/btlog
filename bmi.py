def cal_bmi(height, weight):
    return weight / (height / 100) ** 2

print(cal_bmi(153, 44.5))