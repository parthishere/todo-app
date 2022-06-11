from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import TodoModelForm
from .models import ToDoModel
from tags.models import Tag
from tags.forms import TagForm



# Create your views here.
def list_function(request):
    user = get_user_set(request)
    if user.is_authenticated:
        cat = None
        try:
            cat = Tag.objects.filter(user=user)
        except:
            print('e')
        objects_list = ToDoModel.objects.filter(done=False).filter(archive=False).filter(user=user)
        context = {}
        if objects_list.exists():
            context = {
                'objects_list':objects_list,
                'categories': cat,
            }
    else:
        context = {}
        
    return render(request, 'main_app/home.html', context)

@login_required(login_url='account_login')
def add_todo(request):
    user = get_user_set(request)
    todo_form = TodoModelForm(request.POST, user_set=user)
    tag_form = TagForm(request.POST or None)
    context = {}
    context['form'] = todo_form
    if request.POST:
        if todo_form.is_valid():
            instance = todo_form.save(commit=False)
            instance.user = user
            instance.save()
            context['form'] = todo_form
            return redirect('main_app:home')
        if tag_form.is_valid():
            instance = tag_form.save()
            return redirect('main_app:create')
    return render(request, "main_app/add_todo.html", context=context)


@login_required(login_url='account_login')  
def detail_todo(request, pk=None):
    context = {}
    user = request.user
    if user.is_authenticated:
        obj = get_object_or_404(ToDoModel, pk=pk)
        if obj.user == user:
            if obj is not None:
                context = {
                    'object':obj
                } 
        
    return render(request, 'main_app/detail_todo.html', context=context)
    
    
@login_required(login_url='account_login')        
def edit_todo(request, pk=None):
    instance = get_object_or_404(ToDoModel, pk=pk)
    user = get_user_set(request)
    todo_form = TodoModelForm(request.POST or None, instance=instance, user_set=user)
    context = {}
    context['form'] = todo_form

    if request.POST:
        if todo_form.is_valid():
            instance = todo_form.save(commit=False)
            instance.user = user
            try:
                tag = Tag.objects.prefetch_related(tag__in=request.POST.get('tags'))
                instance.tags.set(tag)
            except:
                pass
            todo_form.save_m2m()
            instance.save()
            return redirect('main_app:home')
    
    return render(request, "main_app/add_todo.html", context=context)   

@login_required(login_url='account_login')
def detail_todo(request, pk=None):
	obj = ToDoModel.objects.filter(pk=pk).filter(user=request.user)
	context = {
		'object':obj
	}
	return render(request, 'main_app/detail_todo.html', context)

@login_required(login_url='account_login')
def delete_list(request, pk=None):
	obj = ToDoModel.objects.filter(pk=pk).filter(user=request.user)
	obj.delete()
	
	return render(request, 'main_app/home.html', {})

@login_required(login_url='account_login')
def done_todo(request):
    if request.POST:
        pk = request.POST.get('pk')
        user = request.user
        if pk is not None:
            obj = get_object_or_404(ToDoModel, pk=pk, user=user)
            if obj.done == True:
                obj.done=False
            else:
                obj.done=True
            obj.save()
            request.session['completed_count'] = ToDoModel.objects.filter(done=True).filter(user=user).count()
            return redirect('main_app:home')
    return render(request, "main_app/home.html", context={})

@login_required(login_url='account_login')
def archives_list(request):
    objects_list = ToDoModel.objects.filter(archive=True).filter(user=request.user)
    context = {
		'objects_list':objects_list
	}
    return render(request, 'main_app/home.html', context=context)

@login_required(login_url='account_login')
def archive_todo(request):
    if request.POST:
        pk = request.POST.get('pk')
        user = request.user
        if pk is not None:
            obj = get_object_or_404(ToDoModel, pk=pk, user=user)
            if obj.archive == True:
                obj.archive=False
            else:
                obj.archive=True
            obj.save()
            request.session['archive_count'] = ToDoModel.objects.filter(archive=True).filter(user=user).count()
            return redirect('main_app:home')
    return render(request, "main_app/home.html", context={})

@login_required(login_url='account_login')
def search_todo(request):
    context = {}
    qs = None
    user = get_user_set(request)
    try:
        cat = Tag.objects.filter(user=user)
        context['categories'] = cat
    except:
        pass
    
    if user.is_authenticated:
        query = request.GET.get('q')
        cat = request.GET.get('category')
        
        if query is not None and cat is None:
            qs = ToDoModel.objects.filter(
                Q(text__icontains=query) |
                Q(start_date__icontains=query) |
                Q(end_date__icontains=query) |
                Q(tags__tag__icontains=query)
            ).filter(user=user)
        
        elif query is None and cat is not None:
            qs = ToDoModel.objects.filter(
               Q(tags__tag__icontains=cat)
            ).filter(user=user)
            
        elif query is not None and cat is not None:
            qs = ToDoModel.objects.filter(
                Q(text__icontains=query) |
                Q(start_date__icontains=query) |
                Q(end_date__icontains=query) |
                Q(tags__tag__icontains=query)
            ).filter(user=user).filter(Q(tags__tag__icontains=query))
        
        if qs is not None:
            context['objects_list'] = qs
            
    else:
        context = {}
        
    return render(request, 'main_app/home.html', context)

@login_required(login_url='account_login')
def done_todo_list(request):
    objects_list = ToDoModel.objects.filter(done=True).filter(user=request.user)
    context = {
		'objects_list':objects_list
	}
    return render(request, 'main_app/home.html', context)


@login_required(login_url='account_login')
def starred_todo(request):
    if request.POST:
        pk = request.POST.get('pk')
        user = request.user
        if pk is not None:
            obj = get_object_or_404(ToDoModel, pk=pk, user=user)
            if obj.starred == True:
                obj.starred=False
            else:
                obj.starred=True
            obj.save()
            request.session['starred_count'] = ToDoModel.objects.filter(starred=True).filter(user=user).count()
            return redirect('main_app:home')
    return render(request, "main_app/home.html", context={})


@login_required(login_url='account_login')
def starred_todo_list(request):
    objects_list = ToDoModel.objects.filter(starred=True).filter(user=request.user)
    context = {
		'objects_list':objects_list
	}
    return render(request, 'main_app/home.html', context)


def get_user_set(request):
    user = request.user
    return user
