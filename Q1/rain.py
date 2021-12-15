# Created By Yair Charit 207282955 #

Rainfull_mi = "45 ,65 ,70.4 ,82.6 ,20.1 ,90.8 ,76.1 ,30.92 ,46.8 ,67.1 ,79.9"
rainy_threshold = 75
res = sum([float(num) > rainy_threshold  for num in Rainfull_mi.split(',')])
print(res)