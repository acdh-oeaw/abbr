from django.shortcuts import render
from webpage.utils import BaseCreateView, BaseUpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_tables2 import RequestConfig
from webpage.utils import GenericListView
from .models import Abbreviation
from .forms import AbbreviationForm, AbbreviationFormHelper
from .tables import AbbreviationTable
from .filters import AbbreviationListFilter


class AbbreviationListView(GenericListView):
    model = Abbreviation
    table_class = AbbreviationTable
    filter_class = AbbreviationListFilter
    formhelper_class = AbbreviationFormHelper
    init_columns = ['id', 'orth', 'expanded', 'lemma', 'pos']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(AbbreviationListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by
        }).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


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
