from django.urls import path
from . import views

urlpatterns = [   
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('pass_change2/', views.pass_change2, name='pass_change2'),
    path('changeData/', views.changeData, name='changeData'),
]