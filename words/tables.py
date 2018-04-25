import django_tables2 as tables
from django_tables2.utils import A

from .models import Abbreviation


class AbbreviationTable(tables.Table):
    id = tables.LinkColumn(
        'words:abbreviation_detail',
        args=[A('pk')], verbose_name='ID'
    )
    orth = tables.LinkColumn(
        'words:abbreviation_detail',
        args=[A('pk')], verbose_name='orth'
    )

    class Meta:
        model = Abbreviation
        sequence = ('id', 'orth', 'expanded', 'lemma', 'pos')
        attrs = {"class": "table table-responsive table-hover"}
