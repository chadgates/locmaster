from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from mylocation.models import Function
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

# Create your views here.


class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = 'mylocation/welcome.html'


class FunctionViewMixin(object):
    model = Function
    context_object_name = 'function'

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        form.instance.creator = self.request.user.username
        messages.info(self.request, self.success_msg)
        return super(FunctionViewMixin, self).form_valid(form)


class FunctionCreate(LoginRequiredMixin, FunctionViewMixin, CreateView):
    success_msg = "Created"
    fields = ['code', 'description']


class FunctionList(LoginRequiredMixin, ListView):
    model = Function
    context_object_name = 'functions'


class FunctionUpdate(LoginRequiredMixin, FunctionViewMixin, UpdateView):
    success_msg = "Saved"
    fields = ['description']

class FunctionDelete(LoginRequiredMixin, FunctionViewMixin, DeleteView):
    success_msg = "Deleted"
    success_url = reverse_lazy('mylocation:function-list')


class FunctionDetail(LoginRequiredMixin, DetailView):
    model = Function
