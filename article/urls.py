from django.urls import path
from article import views

urlpatterns = [
    # class 로 view에서 선언시 "views.class이름.as_view()" 형식으로 써줘야 함
    path('', views.ArticleView.as_view(), name='index'),
]