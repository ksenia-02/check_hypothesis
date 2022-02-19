import csv
import scipy.stats as sps
import math

def get_data():

    with open('Data.csv', 'r', encoding='utf8') as fin:
        reader_object = csv.reader(fin, delimiter=",")
        data = []
        for s in reader_object:
            s = s[0].split(';')
            data.append(int(s[1]))
            if s[0] == '12.06.2020':
                break
        return data, list(map(lambda x : math.log(x), data))

def get_sqr_mean(x : list, y : list):

    return sps.tmean(list(map(lambda x, y: x*y, x, y)))

def get_mean_sqr(x : list, y : list):

    return sps.tmean(x) * sps.tmean(y)

def calc_y(A, b, t):

    return A * math.exp(1)**(b*t)

def split_interval(e : list):

    s = int(math.log2(len(e))) + 1
    step = (max(e) - min(e))/s

    interval = []
    for i in range(s + 1):
        interval.append(min(e) + i * step)
    return interval

if __name__ == '__main__':
    data, x = get_data()
    t = [i+1 for i in range(len(x))]

    x_mean = sps.tmean(x)
    t_mean = sps.tmean(t)

    xt_mean = get_sqr_mean(x, t)
    x_mean_t = get_mean_sqr(x, t)
    t_sqr_mean = get_sqr_mean(t, t)
    t_mean_sqr = get_mean_sqr(t, t)
    b = (xt_mean - x_mean_t)/(t_sqr_mean - t_mean_sqr)
    a = x_mean - b * t_mean

    e = [math.exp(a) * math.exp(b*i) for i in t]
    interval = split_interval(e)
    n = [0] * len(interval)
