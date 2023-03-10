from django.shortcuts import render
from .models import TodoList, TodoItem

from django.contrib.auth.decorators import login_required


@login_required()
def todolist_list_view(request):
    user = request.user
    todolist = TodoList.objects.filter(user=user)
    return render(request, 'list/lists.html', {'todolist': todolist})


@login_required()
def todolist_detail_view(request, pk):
    selected_list = TodoList.objects.get(pk=pk)
    items = selected_list.items
    context = {
        'selected_list': selected_list,
        'items': items.all()
    }
    return render(request, 'list/todolist_items.html', context)
