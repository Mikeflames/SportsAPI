from django.urls import path
from . import views

urlpatterns = [
path('', views.LandingPage.as_view()),          # Landing Page 
path('player/', views.LCplayer.as_view(), name='Players'),
path('player/<int:pk>/', views.RUDplayer.as_view(), name='Player_Edit'),

path('teacher/', views.LCteacher.as_view(), name='Teachers'),
path('teacher/<int:pk>/', views.RUDteacher.as_view(), name='Teacher_Edit'),

path('sport/', views.LCsport.as_view(), name='Sports'),
path('sport/<int:pk>/', views.RUDsport.as_view(), name='Sport_Edit'),

path('player_sports/', views.LCplayer_sport.as_view(), name='Player Sports'),
path('player_sports/<int:pk>/', views.RUDplayer_sport.as_view(), name='Player Sports_Edit'),

path('teacher_sports/', views.LCteacher_sport.as_view(), name='Teacher Sports'),
path('teacher_sports/<int:pk>/', views.RUDteacher_sport.as_view(), name='Teacher Sports_Edit'),

]