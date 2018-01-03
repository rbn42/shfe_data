data = {}
for line in open('data/au.txt'):
    d, name, _open, high, low, close, vol = line.split()
    if d not in data:
        data[d] = []
    data[d].append((_open, high, low, close, vol))
data2={}
for d in data:
    sum_vol, sum_open, sum_high, sum_low, sum_close = 0, 0, 0, 0, 0
    for _open, high, low, close, vol in data[d]:
        vol=float(vol)
        sum_vol += vol
        sum_open += vol * float(_open)
        sum_high += vol * float(high)
        sum_low += vol * float(low)
        sum_close += vol * float(close)
    data2[d]=sum_open/ sum_vol, sum_high / sum_vol, sum_low/ sum_vol, sum_close/ sum_vol, sum_vol
l=list(data2.keys())
l.sort()
for d in l:
    print(d,*data2[d])
