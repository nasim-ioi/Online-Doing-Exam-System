from django.urls import path
from examapp.views import ClassQuestion
from examapp.views import read_csv
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('get_questions/<int:examiner_id>', ClassQuestion.as_view()),
    path('send_answers_and_get_percent/<int:examiner_id>' , csrf_exempt(ClassQuestion.as_view())),
    path('read_csv' , read_csv),
]
