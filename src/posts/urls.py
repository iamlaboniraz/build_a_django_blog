from django.contrib import admin
from django.urls import path
from .views import(
	 post_list,
     post_create,
     post_detail,
     post_update,
     post_delete,
       )

urlpatterns = [
    path('',post_list, name='list'),
    path('create/',post_create, name='create'),
    path('<int:id>/',post_detail, name='detail'),
    path('<int:id>/update/',post_update, name='update'),
    path('<int:id>/delete/',post_delete, name='delete'),
]