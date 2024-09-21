from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('books/', views.books, name='books'),
    path('dic/', views.dic, name='dic'),
    path('todo/', views.todo, name='todo'),
    path('youtube/', views.youtube, name='youtube'),
    path('dnotes/<int:pk>/', views.dnotes, name='dnotes'),
    path('notedetail/<int:pk>/', views.Notesdview.as_view(), name='note_detail'),
    path('homew/', views.homew, name='homew'),
    path('updatehw/<int:pk>/', views.updatehw, name='updatehw'),
    path('updatetd/<int:pk>/', views.updatetd, name='updatetd'),
    path('dhomew/<int:pk>/', views.dhomew, name='dhomew'),
    path('dtodo/<int:pk>/', views.dtodo, name='dtodo'),
    path('conv/', views.conv, name='conv'),
    path('wiki/', views.wiki, name='wiki'),
    path('profile/', views.profile, name='profile'),
]
