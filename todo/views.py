from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ToDo
# Create your views here.


def index(request):
    todo_items = ToDo.objects.all().order_by('-added_date')
    return render(request,'index.html', {'todo_items':todo_items})


def add_todo(request):
    current_time = timezone.now()
    content = request.POST['content']
    ToDo.objects.create(text=content, added_date=current_time)
    print("number of rows in db: ", ToDo.objects.all().count())
    return redirect('/')


def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect("/")
