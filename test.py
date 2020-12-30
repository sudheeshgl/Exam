def hash(key):
    hash = 0
    for i in key:
        hash += ord(i)
    return hash % 30


for i in range(0,30):
    print(i,end='-')
    print(hash('STD-'+str(i)))