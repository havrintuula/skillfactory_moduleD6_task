from django.urls import path
from .views import NewsList, NewsId
urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsId.as_view()),
]
