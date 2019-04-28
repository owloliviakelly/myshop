from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import sqlite3
import logging

logging.basicConfig(filename='log/info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SignUp(generic.CreateView):
    logging.info("signup")
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'