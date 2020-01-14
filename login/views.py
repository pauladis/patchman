from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CompleteUserForm
from django.views.generic import TemplateView


class registerView(TemplateView):

    def get(self, request):
        dict = {}
        form = UserCreationForm()
        dict['form'] = form
        return render(request, 'registration/register.html', dict)

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('complete_register')
        else:
            dict['errors'] = form.errors
        form = UserCreationForm()
        dict['form'] = form
        return render(request, 'registration/register.html', dict)


class complete_registerView(TemplateView):

    def get(self, request):
        dict = {}
        form = CompleteUserForm()
        dict['form'] = form
        return render(request, 'registration/register2.html', dict)

    def post(self, request):
        form = CompleteUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            dict['errors'] = form.errors
        form = CompleteUserForm()
        dict['form'] = form
        return render(request, 'registration/register2.html', dict)