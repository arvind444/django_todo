from django.shortcuts import render, HttpResponse, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	if request.method == "POST":
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
			todo_task = List.objects.all
			messages.success(request,('Item is added to the list.'))
			return render(request, 'home.html', {'todo_task' : todo_task})
		else:
			return render(request, 'error.html')
		
	else:
		todo_task = List.objects.all
		return render(request, 'home.html', {'todo_task' : todo_task})

def delete(request, list_id):
	delete_item = List.objects.get(pk=list_id)
	delete_item.delete()
	messages.success(request,('Item has been deleted.'))
	return redirect('home')

def completed(request, list_id):
	item = List.objects.get(pk=list_id)
	item.finish = True 
	item.save()
	messages.success(request,('You have completed some task'))
	return redirect('home')

def not_completed(request, list_id):
	item = List.objects.get(pk=list_id)
	item.finish = False 
	item.save()
	messages.success(request,('You have forget to complete this task'))
	return redirect('home')

def edit(request, list_id):
	if request.method == "POST":
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			messages.success(request,('Item is edited successfully.'))
			return redirect('home')
		else:
			return render(request, 'error.html')
		
	else:
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item' : item})