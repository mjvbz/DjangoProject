from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


class NewTaskForm(forms.Form):
  task = forms.CharField(label="New task")

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request): 
  return render(request, 'index/index.html', {
    "tasks": tasks
  })

def add_task(request):

  if request.method == 'POST':
    form = NewTaskForm(request.POST)
    if form.is_valid():
      task = form.cleaned_data["task"]
      tasks.append(task)
      return HttpResponseRedirect(reverse("task:index"))
    else:
      return render(request, 'index/add.html', {
        'form': form
        })

  return render(request, 'index/add.html', {
    "form": NewTaskForm()
  }) 