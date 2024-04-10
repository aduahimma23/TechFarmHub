from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import *

class RegisterView(CreateView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm
    success_url = '/login'

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save(commit=True)
        return super().form_valid(form)
    

class LoginView(generic.FormView):
    template_name = 'account/login.html'
    form_class = UserLogin

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        data = request.POST
        if form.is_valid():
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('home'))
            
            return super().post(request, *args, **kwargs)