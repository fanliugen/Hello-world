
dic = {'name':'Logan','age':30,'sex':'male'}

for key in dic.keys():
    print('key={}'.format(key))


for value in dic.values():
    print('value={}'.format(value))

for key,value in dic.items():
    print('{key}:{value}'.format(key=key,value=value))