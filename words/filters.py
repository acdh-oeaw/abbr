import django_filters
from .models import Abbreviation
from vocabs.models import SkosConcept


class AbbreviationListFilter(django_filters.FilterSet):
    orth = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Abbreviation._meta.get_field('orth').help_text,
        label=Abbreviation._meta.get_field('orth').verbose_name
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
