from .import views
from django.urls import path

urlpatterns = [
    path('', views.home , name='home'),
   """ path('books/', views.books , name='books'),
     path('dic/', views.dic , name='dic'),
     path('notes/', views.notes , name='notes'),
     path('todo/', views.todo , name='todo'),
     path('youtube/', views.youtube , name='youtube'),
      path('dnotes/<intk>', views.dnotes , name='dnotes'),
      #path('notedetail/<int=pk>', views.Notesdview.as_view(), name='note_detail' ),
       path('homew/', views.homew , name='homew'),
       path('updatehw/<int=pk>', views.updatehw , name='updatehw'),
        path('updatetd/<int=pk>', views.updatetd , name='updaterd'),
        path('dhomew/<int=pk>', views.dhomew , name='dhomew'),
         path('dtodo/<intk>', views.dtodo , name='dtodo'),
          path('conv/', views.conv , name='conv'),"""
]