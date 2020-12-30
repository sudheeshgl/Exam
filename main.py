import csv


class HashTable():
    def __init__(self):
        self.max_question=30
        self.table=[None] * self.max_question
    def __setitem__(self, key, value):
        hashKey=self.__hash(key)
        newhashKey=self.__check(hashKey)
        data = (hashKey,key,value)
        try:
            if self.table[hashKey][1] != key:
                self.table[newhashKey] = data
            else:
                print(f'Already added {key}')
        except:
            self.table[newhashKey] = data

    def __getitem__(self, key):
        newkey=self.__hash(key)
        if self.table[newkey] is not None and self.table[newkey][0] == newkey and self.table[newkey][1] == key :
            return self.table[newkey]
        else:
            try:
                while self.table[newkey][1] != key:
                    newkey=self.__increment(newkey)
            except:
                return None
            return self.table[newkey]
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


if __name__ == '__main__':
    h=HashTable()
    with open('AnswerSheet.csv', 'r') as sheet, open('Answer.csv', 'r') as answer:
        datas = csv.DictReader(sheet)
        ans = csv.DictReader(answer)
        ans = [i for i in ans]
        for data in datas:
            student = []
            regNo = data['Register No']
            score = 0
            negativeScore = 0
            student.append(data['Name'])
            for i in range(1, 11):
                if ans[0][str(i)] == data[str(i)]:
                    score += 1
                else:
                    negativeScore += 1
            student.append(score)
            student.append(negativeScore)
            h[regNo]=student

    for i in h.table:
        print(i)
    print(h['REG-002'])
