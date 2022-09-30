from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.details, name='details'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('write/', views.write, name='write'),
    path('detail/<int:review_pk>', views.detail, name='detail'),
    path('edit/<int:review_pk>', views.edit, name='edit'),
    path('upadte/<int:review_pk>', views.update, name='update'),
    path('delete/<int:review_pk>', views.delete, name='delete'),
]
