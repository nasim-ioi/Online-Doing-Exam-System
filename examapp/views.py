import csv
import json
import random

from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from examapp.models import Examiner, Questions

# Create your views here.

def read_csv(requset): 
    if requset.method == 'GET': 
        with open("/home/nasim/cvv.csv" , mode = 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = Questions(question = row["question"] , options = row["options"] , correct_option = row["correct_option"])
                q.save()
        return JsonResponse({"result" : "done"})
    
class ClassQuestion(View):

    def get(self, request, examiner_id):
        l = []
        return_list = []
        ran_list = random.sample(range(2,25) , 20)
        for r in ran_list:
            l.append(Questions.objects.get(id = int(r)))
        obj = Examiner.objects.get(id = int(examiner_id))
        obj.examiner_questions = str(l)
        for r in l:
            return_list.append({"id" : r.id , "question" : r.question , "options" : r.options})
        return JsonResponse({"result" : return_list})
        # response = FileResponse(open('/home/nasim/mocktest.txt', 'rb'))
        # return response 

    def post(self , request , examiner_id):
        correct = 0
        wrong = 0
        not_answer = 0
        msg = request.body.decode('utf-8')
        jsonmsg = json.loads(msg)
        obj = Examiner.objects.get(id = examiner_id)
        obj.examiner_questions = str(jsonmsg)
        for qid , anso in jsonmsg.items():
            objq = Questions.objects.get(id = qid)
            if str(objq.correct_option) == str(anso):
                correct += 1
            else:
                wrong += 1
        not_answer = 20 - len(jsonmsg)
        percent = (correct*3 - wrong)/(20*3) * 100
        return JsonResponse({"your percent" : percent , "wrong ansewrs" : wrong , "correct answer" : correct , "nazade" : not_answer})


# /home/nasim/my codes linux/django2codes/exam/examapp