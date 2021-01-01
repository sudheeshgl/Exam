from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from configparser import ConfigParser
from .calculate import run

config = ConfigParser()
# Create your views here.
def home(request):
    return render(request,'index.html')

def calculate(request):
    totalstudent = request.POST.get('totalstudents')
    noofquestions = request.POST.get('noofquestions')
    categories = request.POST.get('categories')
    if request.FILES['studnetAnswerSheet'] and  request.FILES['AnswerSheet']:
        studnetAnswerSheet = request.FILES['studnetAnswerSheet']
        AnswerSheet = request.FILES['AnswerSheet']
        fs = FileSystemStorage()
        fs.save(studnetAnswerSheet.name, studnetAnswerSheet)
        fs.save(AnswerSheet.name, AnswerSheet)
    config['exam']={}
    config['exam']['TotalStudents']=totalstudent
    config['exam']['NoOfQuestion']=noofquestions
    config['exam']['Categories']=categories
    config['exam']['AnswerSheet']=studnetAnswerSheet.name
    config['exam']['Answer']=AnswerSheet.name
    with open('config.ini', 'w') as f:
        config.write(f)
    data=run()
    count=[i for i in range(1,len(data))]
    return render(request,'index.html',{'totalrank':data[0],'categories':data[1:],'count':count})