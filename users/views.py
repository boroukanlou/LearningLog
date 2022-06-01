from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            newUser = form.save()
            login(request, newUser)
            return redirect('Notes:home_page')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)