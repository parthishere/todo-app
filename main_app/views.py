from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import TodoModelForm
from .models import ToDoModel

# Create your views here.
def list_function(request):
	objects_list = ToDoModel.objects.all()
	context = {
		'objects_list':objects_list
	}
	return render(request, 'main_app/home.html', context)

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


def detail_todo(request, pk=None):
	obj = ToDoModel.objects.filter(pk=pk)
	context = {
		'obj':obj
	}
	return render(request, 'main_app/home.html', context)

def delete_list(request, pk=None):
	obj = ToDoModel.objects.filter(pk=pk)
	context = {
		'obj':obj
	}
	
	return render(request, 'main_app/home.html', context)


def archives_list(request):
    pass

def archive_todo(request):
    pass

def search_todo(request):
    pass