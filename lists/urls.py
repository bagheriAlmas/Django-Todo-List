from .views import todolist_list_view
from django.urls import path

urlpatterns = [
    path('', todolist_list_view, name='lists')
]
