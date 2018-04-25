from django.shortcuts import render
from webpage.utils import BaseCreateView, BaseUpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

from .models import Abbreviation
from .forms import AbbreviationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class AbbreviationDetailView(DetailView):
    model = Abbreviation
    template_name = 'words/abbreviation_detail.html'


class AbbreviationCreate(BaseCreateView):

    model = Abbreviation
    form_class = AbbreviationForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AbbreviationCreate, self).dispatch(*args, **kwargs)


class AbbreviationUpdate(BaseUpdateView):

    model = Abbreviation
    form_class = AbbreviationForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AbbreviationUpdate, self).dispatch(*args, **kwargs)


class AbbreviationDelete(DeleteView):
    model = Abbreviation
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_sites')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AbbreviationDelete, self).dispatch(*args, **kwargs)
