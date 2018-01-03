import glob
import re
l = glob.glob('./data/*.csv')
l.sort()
for p in l:
    isau = False
    auname = None
    for line in open(p):
        item = line.split(',')
        name = item[0]
        if len(name) > 0:
            if len(re.findall('au\d\d\d\d', name)) > 0:
                auname = name
                isau = True
            else:
                isau = False
        if isau:
            _, d, _, _, _open, high, low, close, _, _, _, vol = item[:12]
            if len(_open) < 1:
                _open = 0
            if len(high) < 1:
                high = 0
            if len(low) < 1:
                low = 0
            if len(vol)<1:
                vol=0
            if len(close)<1:
                close=0
            if len(d)<1:
                continue
            print(d, auname, _open, high, low, close, vol)
