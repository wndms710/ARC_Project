t = '#Parameters = {thARC=0; nARC=2; thsub=1; p=1; nSub=1}'

a = t.split(' ')


array = [] 

array.append(a[6][5:-1])    # nSub
array.append(a[3][5:-1])    # nARC
array.append(a[2][7:-1])    # thARC

print(array)
