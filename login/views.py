from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CompleteUserForm


#def login(request):
#    from pdb import set_trace
#    set_trace()
#    return render(request, 'login.html')

def register(request):
    dict = {}
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('complete_register')
        else:
            dict['errors'] = form.errors
    form = UserCreationForm()
    dict['form'] = form
    return render(request, 'registration/register.html', dict)

def complete_register(request):
    dict = {}
    if request.method == 'POST':
        form = CompleteUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            dict['errors'] = form.errors
    form = CompleteUserForm()
    dict['form'] = form
    return render(request, 'registration/register2.html', dict)
