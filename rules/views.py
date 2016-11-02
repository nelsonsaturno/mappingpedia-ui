# from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import *
from rules.forms import *


class UploadRules(FormView):
    template_name = 'rules/upload_rules.html'
    form_class = UpdateRulesForm
    success_url = reverse_lazy('upload_success')

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            return HttpResponseRedirect(reverse_lazy('upload_success'))
        else:
            print form
            return self.form_invalid(form)


class UploadSuccess(TemplateView):
    template_name = 'rules/upload_success.html'
