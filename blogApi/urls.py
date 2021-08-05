from django.urls import path
# from rest_framework import views
from blogApi import views

urlpatterns = [
    path('blog', views.post_list,),
    path('blog/post/<int:pk>', views.post_detail),
    path('', views.BlogView.as_view()),

]