from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('read_csv/', read_csv),
    path('singup/', SingUp.as_view()),
    path('login/', UserLoginApiview.as_view()),
    path('ans/', GetUserAnswers.as_view())
]

router.register('questions', QuestionsListViewSet)
urlpatterns += router.urls