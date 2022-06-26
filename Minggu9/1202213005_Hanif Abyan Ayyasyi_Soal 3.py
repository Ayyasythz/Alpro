def cek_prim(a):
    if a > 1:
        for i in range(2, int(a / 2) + 1):
            if (a % i) == 0:
                return False
        else:
            return True
    else:
        return True


def bil_prima(awal, akhir):
    list_prima = []
    for x in range(awal, akhir + 1):
        if cek_prim(x):
            list_prima.append(x)

    a = 0
    for x in list_prima:
        a += 1

    return a


c = bil_prima(1, 30)
print(c)
