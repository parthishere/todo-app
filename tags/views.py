from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Tag
from .forms import TagForm

@login_required(login_url='account_login')
def add_tag(request):
    tag_form = TagForm(request.POST or None)
    context = {}
    context['form'] = tag_form
    if request.POST:
        if tag_form.is_valid():
            instance = tag_form.save(commit=False)
            instance.user = request.user
            instance.save()
            context['form'] = tag_form
            return redirect('main_app:home')
    
    return render(request, "main_app/add_todo.html", context=context)



@login_required(login_url='account_login')        
def edit_tag(request, pk=None):
    instance = get_object_or_404(Tag, pk=pk)
    tag_form = TagForm(request.POST or None, instance=instance)
    context = {}
    context['form'] = tag_form
    if request.POST:
        if tag_form.is_valid():
            instance = tag_form.save(commit=False)
            instance.user = request.user
            instance.save()
            context['form'] = tag_form
            return redirect('main_app:home')
    
    return render(request, "main_app/add_todo.html", context=context)

@login_required(login_url='account_login')
def delete_tag(request, pk=None):
	obj = Tag.objects.filter(pk=pk)
	obj.delete()
	
	return render(request, 'main_app/home.html', {})
