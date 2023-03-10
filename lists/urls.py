from .views import todolist_list_view,todolist_detail_view
from django.urls import path

urlpatterns = [
    path('', todolist_list_view, name='lists'),
    path('<int:pk>/', todolist_detail_view, name='list_items')
]
