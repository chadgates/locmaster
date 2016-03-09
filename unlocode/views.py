from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from unlocode.models import LocVersion, Locode
from unlocode.initializedata import populateInitial
from unlocode.csvimport import check_version_dir
from unlocode.tasks import importVersion
from django.db.models import Q
import os

class UnLocVersionMixin(object):
    model = LocVersion
    fields = ['version']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(UnLocVersionMixin, self).form_valid(form)


class UnLocVersionDetail(LoginRequiredMixin, DetailView):
    model = LocVersion
    context_object_name = 'version'
    def get_context_data(self, **kwargs):
        context = super(UnLocVersionDetail,self).get_context_data(**kwargs)
        context["files"]=check_version_dir(str(self.kwargs.get('pk')))
        context['complete']=not(False in dict(context["files"]).values())
        return context

class UnLocodeSearch(LoginRequiredMixin, ListView):
    model = Locode
    context_object_name = "unlocode"
    queryset = Locode.objects.none()
    template_name = 'unlocode/locode_search.html'

    def get_queryset(self):
        queryset = super(UnLocodeSearch, self).get_queryset()

        q = self.request.GET.get("q")
        if q:

            return Locode.objects.filter(
                Q(locode__iexact=q)|
                Q(locname__istartswith=q) |
                Q(locnamewodia__istartswith=q)).order_by('locode', 'version').distinct('locode')

        return queryset



class UnLocodeList(LoginRequiredMixin, ListView):
    model = Locode
    context_object_name = 'unlocode'
    allow_empty = False

    def get_queryset(self):
        return Locode.objects.filter(locode=self.kwargs.get('locode')).order_by("version")

    def get_context_data(self, **kwargs):
        context = super(UnLocodeList, self).get_context_data(**kwargs)
        context["thelocode"] = self.kwargs.get('locode')
        return context


class UnLocVersionList(LoginRequiredMixin, ListView):
    model = LocVersion
    context_object_name = 'version_list'
    queryset = LocVersion.objects.order_by("-version")



class UnLocVersionCreate(LoginRequiredMixin, UnLocVersionMixin, CreateView):
    success_msg = "Created"

    def form_valid(self, form):
        form.instance.creator = self.request.user.username
        return super(UnLocVersionCreate, self).form_valid(form)


class UnLocVersionUpdate(LoginRequiredMixin, UnLocVersionMixin, UpdateView):
    success_msg = "Updated"

    def post(self, request, *args, **kwargs):
        if 'load' in request.POST:
            importVersion.delay(str(self.kwargs.get('pk')))
            messages.info(request, "Background Job Started, come back to see if it is done")
            #messages.info(request, importUNLOCODE(str(self.kwargs.get('pk'))))
            return super(UnLocVersionUpdate, self).get(request, *args, **kwargs)
        else:
            return super(UnLocVersionUpdate, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UnLocVersionUpdate,self).get_context_data(**kwargs)
        context["files"]=check_version_dir(str(self.kwargs.get('pk')))
        context['complete']=not(False in dict(context["files"]).values())
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user.username
        return super(UnLocVersionUpdate, self).form_valid(form)


class UnLocVersionDelete(LoginRequiredMixin, UnLocVersionMixin, DeleteView):
    success_msg = "Deleted"
    success_url = reverse_lazy('unlocode:list')


class Populate(TemplateView):

    template_name = 'unlocode/populate.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        messages.info(request, populateInitial())
        return super(TemplateView, self).render_to_response(context)


class LocodeInfo(TemplateView):

    template_name = 'unlocode/locode_info.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(LocodeInfo,self).get_context_data(**kwargs)
        context["info"] = os.getcwd() + "/unlocode/data/versions/TEST-1"
        return context
