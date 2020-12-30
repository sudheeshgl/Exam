import csv

with open('AnswerSheet.csv','r') as sheet , open('Answer.csv','r') as answer:
    datas=csv.DictReader(sheet)
    ans=csv.DictReader(answer)
    ans=[i for i in ans]
    for data in datas:
        for answerSheet in data:
            print(data[answerSheet])
