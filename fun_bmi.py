# BMI 健康分类程序
# 功能：定义 fun_bmi 函数，输入姓名、身高、体重，
# 计算 BMI 指数并按四档给出健康提示

def fun_bmi(name, height, weight):
    print(name + '的身高：' + str(height) + '米，体重：' + str(weight) + '千克')
    bmi = weight / (height * height)
    print(name + '的bmi为:' + str(bmi))
    if bmi < 18.5:
        print('体重过轻')
    if bmi >= 18.5 and bmi < 24.9:
        print('正常范围')
    if bmi >= 24.9 and bmi < 29.9:
        print('体重过重')
    if bmi >= 29.9:
        print('肥胖')

fun_bmi("Zhang San", 1.7, 60)
fun_bmi("Li Si", 1.8, 85)
fun_bmi("Zhao Wu", 1.9, 95)
