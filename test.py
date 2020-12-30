import csv

with open('AnswerSheet.csv','r') as sheet , open('Answer.csv','r') as answer:
    datas=csv.DictReader(sheet)
    ans=csv.DictReader(answer)
    ans=[i for i in ans]
    for data in datas:
        student=[]
        regNo=data['Register No']
        score=0
        negativeScore=0
        student.append(data['Name'])
        for i in range(1,11):
            if ans[0][str(i)]==data[str(i)]:
                score+=1
            else:
                negativeScore+=1
        student.append(score)
        student.append(negativeScore)
        print(student)
