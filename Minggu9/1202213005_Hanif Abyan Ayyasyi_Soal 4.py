listangka = [3.11013, 5.57688, 4.00914, 7.24241, 9.01344, 8.56773, 6.67774]
listVolume = list(map(lambda y: y*y*y, listangka))

list_komadua = list(map(lambda x: round(x, 2), listVolume))
print(list_komadua)
