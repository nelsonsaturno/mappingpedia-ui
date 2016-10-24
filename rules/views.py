from django.shortcuts import render
from django.views.generic import TemplateView


class MainMenu(TemplateView):
    template_name = 'rules/main_menu.html'
