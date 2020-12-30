import csv
from configparser import ConfigParser

config = ConfigParser()
config.read('config.txt')

class HashTable():
    def __init__(self):
        self.max_students = int(config.get('exam','Total Students'))
        self.table=[None] * self.max_students
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
        return hash % self.max_students

    def __increment(self,key):
        return (key + 1) % self.max_students

    def __check(self,key):
        if self.table[key] is None:
            return key
        else:
            while self.table[key] is not None:
                key=self.__increment(key)
            return key

    def Splitcategories(self):
        categories = list(map(int, config.get('exam', 'categories').split(',')))
        totalcat=0
        for i in categories:
            totalcat+=i
        temp=[]
        for category in categories:
            temp.append(int(category*config.getint('exam','No of Question')/totalcat))
        return temp

if __name__ == '__main__':
    h=HashTable()
    with open(config.get('exam','Answer Sheet'), 'r') as sheet, open(config.get('exam','Answer'), 'r') as answer:
        datas = csv.DictReader(sheet)
        ans = csv.DictReader(answer)
        ans = [i for i in ans]
        categories = h.Splitcategories()
        print(categories)
        for data in datas:
            student = []
            regNo = data['Register No']
            TotalScore=TempScore=TotalNegativeScore=TempNegativeScore=count2=unAnswer=0
            count=1
            NegativeScore=[]
            Score=[]
            for i in range(1, int(config.getint('exam','No of Question')+1)):
                if len(data[str(i)]) == 0:
                    unAnswer+=1
                    pass
                elif ans[0][str(i)] == data[str(i)]:
                    TotalScore += 1
                    TempScore +=1
                else:
                    TotalNegativeScore += 1
                    TempNegativeScore += 1
                if count == categories[count2]:
                    Score.append(TempScore)
                    NegativeScore.append(TempNegativeScore)
                    TempNegativeScore = 0
                    TempScore = 0
                    count2+=1
                    count=0
                count+=1

            student.append(data['Name'])
            student.append(Score)
            student.append(NegativeScore)
            student.append(TotalScore)
            student.append(TotalNegativeScore)
            student.append(unAnswer)
            h[regNo]=student


    for i in h.table:
        print(i)

