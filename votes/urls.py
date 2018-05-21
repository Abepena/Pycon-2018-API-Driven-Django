from django.urls import path
from . import views

urlpatterns = [
    path('', views.VoteList.as_view(), name = 'votes')

]