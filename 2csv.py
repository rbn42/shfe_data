import glob
l=glob.glob('./data/*.xls')
for n in l:
    print('ssconvert %s %s.csv'%(n,n))
