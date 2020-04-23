import django_filters
from .models import Abbreviation
from vocabs.models import SkosConcept


class AbbreviationListFilter(django_filters.FilterSet):
    orth = django_filters.CharFilter(
        lookup_expr='exact',
        help_text='exact search',
        label='exact and case sensitive search'
        )
    orth_fuzzy = django_filters.CharFilter(
        field_name="orth",
        lookup_expr='icontains',
        help_text='Fuzzy search',
        label='Fuzzy search and ignore case'
        )
    expanded = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Abbreviation._meta.get_field('expanded').help_text,
        label=Abbreviation._meta.get_field('expanded').verbose_name
        )
    lemma = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Abbreviation._meta.get_field('lemma').help_text,
        label=Abbreviation._meta.get_field('lemma').verbose_name
        )
    pos = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.all(),
        help_text=Abbreviation._meta.get_field('pos').help_text,
        label=Abbreviation._meta.get_field('pos').verbose_name
        )

    class Meta:
        model = Abbreviation
        fields = '__all__'
