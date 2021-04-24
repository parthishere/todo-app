from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import TodoModelForm
from .models import ToDoModel

# Create your views here.
def list_function(request):
    if request.user.is_authenticated:
        objects_list = ToDoModel.objects.filter(done=False).filter(archive=False).filter(user=request.user)
        context = {}
        if objects_list.exists():
            context = {
                'objects_list':objects_list
            }
    else:
        context = {}
        
    return render(request, 'main_app/home.html', context)

@login_required(login_url='account_login')
def add_todo(request):
    todo_form = TodoModelForm(request.POST or None)
    context = {}
    context['form'] = todo_form
    if request.POST:
        if todo_form.is_valid():
            instance = todo_form.save(commit=False)
            instance.user = request.user
            instance.save()
            context['form'] = todo_form
            return redirect('main_app:home')
    
    return render(request, "main_app/add_todo.html", context=context)
    
@login_required(login_url='account_login')        
def edit_todo(request, pk=None):
    instance = get_object_or_404(ToDoModel, pk=pk)
    todo_form = TodoModelForm(request.POST or None, instance=instance)
    context = {}
    context['form'] = todo_form
    if request.POST:
        if todo_form.is_valid():
            instance = todo_form.save(commit=False)
            instance.user = request.user
            instance.save()
            context['form'] = todo_form
            return redirect('main_app:home')
    
    return render(request, "main_app/add_todo.html", context=context)   

@login_required(login_url='account_login')
def detail_todo(request, pk=None):
	obj = ToDoModel.objects.filter(pk=pk)
	context = {
		'obj':obj
	}
	return render(request, 'main_app/home.html', context)

@login_required(login_url='account_login')
def delete_list(request, pk=None):
	obj = ToDoModel.objects.filter(pk=pk)
	obj.delete()
	
	return render(request, 'main_app/home.html', {})

@login_required(login_url='account_login')
def done_todo(request):
    if request.POST:
        print('h')
        pk = request.POST.get('pk')
        if pk is not None:
            print('i')
            obj = get_object_or_404(ToDoModel, pk=pk)
            if obj.done == True:
                obj.done=False
            else:
                obj.done=True
            obj.save()
            request.session['completed_count'] = ToDoModel.objects.filter(done=True).count()
            return redirect('main_app:home')
    return render(request, "main_app/home.html", context={})

@login_required(login_url='account_login')
def archives_list(request):
    objects_list = ToDoModel.objects.filter(archive=True)
    context = {
		'objects_list':objects_list
	}
    return render(request, 'main_app/home.html', context=context)

@login_required(login_url='account_login')
def archive_todo(request):
    if request.POST:
        pk = request.POST.get('pk')
        if pk is not None:
            obj = get_object_or_404(ToDoModel, pk=pk)
            if obj.archive == True:
                obj.archive=False
            else:
                obj.archive=True
            obj.save()
            request.session['archive_count'] = ToDoModel.objects.filter(archive=True).count()
            return redirect('main_app:home')
    return render(request, "main_app/home.html", context={})

@login_required(login_url='account_login')
def search_todo(request):
    context = {}
    qs = None
    if request.user.is_authenticated:
        query = request.GET.get('q')
        if query is not None:
            qs = ToDoModel.objects.filter(
                Q(text__icontains=query) |
                Q(start_date__icontains=query) |
                Q(end_date__icontains=query) |
                Q(tags__tag__icontains=query)
            ).filter(user=request.user)
            
        
        if qs is not None:
            context = {
                'objects_list':qs
            }
    else:
        context = {}
        
    return render(request, 'main_app/home.html', context)

@login_required(login_url='account_login')
def done_todo_list(request):
    objects_list = ToDoModel.objects.filter(done=True)
    context = {
		'objects_list':objects_list
	}
    return render(request, 'main_app/home.html', context)