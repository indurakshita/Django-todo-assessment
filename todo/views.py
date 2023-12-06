from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.

def home(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo added successfully!")
            return redirect('home')

    data = Todo.objects.all()
    print(data)
    context = {
        "forms": form,
        "data": data,    
    }

    return render(request, 'home.html', context)

def remove(request, id):
    item = get_object_or_404(Todo, id=id, user=request.user)
    item.delete()
    messages.info(request, "Item removed successfully.")
    return redirect('home')


def complete(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    messages.info(request, "Item mark as completed.")
    return redirect('home')