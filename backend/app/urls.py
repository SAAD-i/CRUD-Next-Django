from django.urls import path
from .views import StudentView
urlpatterns = [
    path('get',StudentView.as_view(),name='getStudent'),
    path('delete/<int:pk>',StudentView.as_view(),name='deleteStudent'),
    path('post',StudentView.as_view(),name='addStudent'),
    path('put/<int:pk>',StudentView.as_view(),name='updateStudent'),
]
