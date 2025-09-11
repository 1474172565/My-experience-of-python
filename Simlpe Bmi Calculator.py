use_height = float(input("身高(m)：" ))
use_weight = float(input("体重(kg)：" ))
Bmi = use_weight/((use_height) ** 2)
print("你的Bmi是" + str(Bmi))
if float(Bmi) <= 25 and float(Bmi) >= 21:
    print("You are fine. Thank you, and you")