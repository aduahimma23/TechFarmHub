from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import UserLogin, UserRegistrationForm

class RegisterView(CreateView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
    

class LoginView(generic.FormView):
    template_name = 'account/login.html'
    form_class = UserLogin

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
        
        form.add_error(None, 'Invalid username or password')
        return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')