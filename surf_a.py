
def surf_a(x, y, z):
    print("长方体的长为：" + str(x) + "，宽为：" + str(y) + "，高为：" + str(z))
    s = 2 * (x * y + x * z + y * z)
    print("表面积为" + str(s))



surf_a(x=8, y=2, z=6)
