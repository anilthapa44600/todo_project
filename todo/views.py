from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import ToDo
# Create your views here.


@login_required(login_url='login')
def index(request):
        keys_list = request.GET.keys()
        # print(keys_list)
        if 'status' in keys_list:
            status = request.GET['status']
            todo_items = ToDo.objects.filter(user=request.user ,status=status).order_by('-added_date')
        elif 'priority' in keys_list:
            priority = request.GET['priority']
            todo_items = ToDo.objects.filter(user=request.user, priority=priority).order_by('-added_date')
        else:
            todo_items = ToDo.objects.filter(user=request.user).order_by('-added_date')
        return render(request,'index.html', {'todo_items': todo_items})


@login_required(login_url='login')
def add_todo(request):
    if request.method == 'POST':
        current_time = timezone.now()
        print(request.POST)
        ToDo.objects.create(text=request.POST.get('content'),
                            added_date=current_time,
                            priority=request.POST.get('priority', 'normal'),
                            user=request.user)
        print("number of rows in db: ", ToDo.objects.all().count())
        return redirect('/')
    return HttpResponse('<h1>Unable to process the request</h1>')


@login_required(login_url='login')
def update_todo(request, todo_id):
    if request.method == 'GET':
        todo_item = ToDo.objects.get(id=todo_id)
        print("todo_item:", todo_item.status)
        return JsonResponse({'id': todo_item.id, 'text': todo_item.text, 'priority': todo_item.priority,
                             'status': todo_item.status, 'added-date': todo_item.added_date})
    elif request.method == 'POST':
        print("DATA FOR UPDATE:")
        print(request.POST)
        keys_list = request.POST.keys()
        # if 'status' in keys_list:
        #     status = 1
        # else:
        #     status = 0
        if request.POST.get('status', None):
            status = 1
        else:
            status = 0
        ToDo.objects.filter(id=todo_id).update(text=request.POST['content'], priority=request.POST['priority'],
                                               status=status)
        return redirect('/')


@login_required(login_url='login')
def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect("index")
