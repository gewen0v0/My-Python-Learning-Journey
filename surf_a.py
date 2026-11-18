# 长方体表面积计算
# 功能：定义 surf_a 函数，输入长、宽、高，计算并输出长方体的表面积

def surf_a(x, y, z):
    print("长方体的长为：" + str(x) + "，宽为：" + str(y) + "，高为：" + str(z))
    s = 2 * (x * y + x * z + y * z)
    print("表面积为" + str(s))



surf_a(x=8, y=2, z=6)
