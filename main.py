class HashTable():
    def __init__(self):
        self.max_question=100
        self.table=[None] * self.max_question

    def __setitem__(self, key, value):
        hashKey=self.__hash(key)
        newhashKey=self.__check(hashKey)
        data = (hashKey,key,value)
        self.table[newhashKey] = data

    def __getitem__(self, key):
        newkey=self.__hash(key)
        if self.table[newkey] is not None and self.table[newkey][0] == newkey and self.table[newkey][1] == key :
            return self.table[newkey]
        else:
            return 1

    def __hash(self,key):
        hash=0
        for i in key:
            hash+=ord(i)
        return hash % self.max_question

    def __increment(self,key):
        return (key + 1) % self.max_question

    def __check(self,key):
        if self.table[key] is None:
            return key
        else:
            while self.table[key] is not None:
                key=self.__increment(key)
            return key
h= HashTable()
h['STD-1'] = ('SUDHEESH',[10,4,3,2,1],96,4)
h['STD-2'] = ('Ananthan',[10,4,3,2,1],96,4)
print(h['STD-1'])
print(h['STD-2'])
for i in h.table:
    print(i)

