from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from djangousers.models import Contact


class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'
