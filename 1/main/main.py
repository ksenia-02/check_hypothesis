import scipy
import csv
import math
from statistics import mean
way = "/content/data.csv"
rawdata = list()
with open(way) as f: # выдираю из csv количества смертей за 90 дней начиная с февраля 21го
#если открывать csv в экселе, то это будет 328я строка
    reader = csv.reader(f)
    i = 1
    for row in reader:
        if(i<328):
            i += 1
        else:
            if(i<(328+90)):
                rawdata += [math.log(float(row[1]))] # x[i] = ln(y[i])
                i += 1
            else:
                break

x = mean(rawdata) # среднее x
t = 45 # среднее t
xt = list() # здесь потом будет среднее x*t
i = 1 #отсюда и далее я буду использовать i в качестве t
for num in rawdata: # заполняю x*t
    xt += [num*float(i)]
    i += 1
xt = mean(xt)
i = 1
t2 = list()
while i <= 90: 
    t2 += [i*i]
    i += 1
t2 = mean(t2) # среднее из t^2
b = xt-x*t
b /= t2-45*45
a = x - b*t
A = math.exp(a) # A = e^a
epsilon = list() # начинаю считать дисперсию погрешности
epsilon2 = list()
for d in rawdata:
    num = math.exp(d) - A*math.exp(b*i)
    epsilon += [num]
    epsilon2 +=[num**2]
epsilon = mean(epsilon)**2
epsilon2 = mean(epsilon2)
print("epsilon = ", epsilon2-epsilon)
i = 1
for d in rawdata: # вывожу сначала реальное число из датасета, а через пробел - рассчитанное
    print(math.exp(d), " ", A*math.exp(b*i))
    i += 1