from rest_framework import viewsets
from .models import Abbreviation
from .serializers import AbbreviationSerializer
from .filters import AbbreviationListFilter


class AbbreviationViewSet(viewsets.ModelViewSet):
    queryset = Abbreviation.objects.all()
    serializer_class = AbbreviationSerializer
    filter_class = AbbreviationListFilter
