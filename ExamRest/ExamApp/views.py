from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
import random
import csv
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def read_csv(request):
    with open("/home/nasim/cvv.csv" , mode = 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            q = Questions(question = row["question"] , options = row["options"] , correct_option = row["correct_option"])
            q.save()
    return Response({"the action has been done"})

class SingUp(APIView):
    serializer_class = SingUpSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            try : 
                user = User.objects.create(username = username)
            except Exception as e:
                return Response(str(e))
            else:
                user.set_password(password)
                token = Token.objects.create(user = user)
                user.save()
                return Response("{} is created with pasword : {} with token : {}".format(username, password, token.key))

class UserLoginApiview(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
                
class QuestionsListViewSet(ReadOnlyModelViewSet):
    ran_list_str = []
    ran_list = random.sample(range(97,121) , 10)
    for i in ran_list:
        ran_list_str.append(str(i))

    queryset = Questions.objects.filter(id__in = ran_list_str)

    serializers = {
        'list' : QuestionSerializer,
        'retrieve' : QuestionDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action)

class GetUserAnswers(APIView):
    serializer_class = AnsewrSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):

            validated_data_dict = dict(serializer.validated_data)
            value_of_dict = validated_data_dict['ansewr']

            correct = 0
            wrong = 0
            not_answer = 0

            for qid, ans in value_of_dict.items():
                print(qid, ' ', ans)
                q =  Questions.objects.get(id = qid)
                if ans == q.correct_option:
                    correct += 1
                else:
                    wrong += 1
            not_answer = 10 - len(value_of_dict)
            percent = (correct*3 - wrong)/(10*3) * 100

            return Response("your percent : {} wrong ansewrs : {} correct answer : {} nazade : {}".format(percent, wrong, correct, not_answer))


