from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ToDo
# Create your views here.


def index(request):
    keys_list = request.GET.keys()
    print(keys_list)
    if 'status' in keys_list:
        status = request.GET['status']
        todo_items = ToDo.objects.filter(status=status).order_by('-added_date')
    elif 'priority' in keys_list:
        priority = request.GET['priority']
        todo_items = ToDo.objects.filter(priority=priority).order_by('-added_date')
    else:
        todo_items = ToDo.objects.all().order_by('-added_date')
    return render(request,'index.html', {'todo_items': todo_items})


def add_todo(request):
    current_time = timezone.now()
    content = request.POST['content']
    ToDo.objects.create(text=content, added_date=current_time)
    print("number of rows in db: ", ToDo.objects.all().count())
    return redirect('/')


def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect("/")
