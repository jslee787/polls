from django.urls import path
from control import views
#네임 스페이스(소속공간)
app_name = 'control'

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/poll/
    path('register/', views.register, name='register')
]