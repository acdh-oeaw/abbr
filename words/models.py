from django.db import models
from django.urls import reverse
from idprovider.models import IdProvider
from vocabs.models import SkosConcept


class Abbreviation(IdProvider):
    orth = models.CharField(
        max_length=300, blank=True, null=True,
        verbose_name="ORTH", help_text="equals spaCy's ORTH"
    )
    expanded = models.CharField(
        max_length=300, blank=True, null=True,
        verbose_name="resolved abbreviation", help_text="The resolved abbrevation"
    )
    lemma = models.CharField(
        max_length=300, blank=True, null=True,
        verbose_name="LEMMA", help_text="The abbreviation's normalized form"
    )
    pos = models.ForeignKey(
        SkosConcept, blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name="POS", help_text="The abbreviation's Part of Speech tag"
    )

    @classmethod
    def get_createview_url(self):
        return reverse('words:abbreviation_create')

    def get_absolute_url(self):
        return reverse(
            'words:abbreviation_detail', kwargs={'pk': self.id}
        )

    def __str__(self):
        if self.expanded:
            return "{} ({})".format(self.orth, self.expanded)
        else:
            return "{}".format(self.orth)

    def get_next(self):
        next = Abbreviation.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Abbreviation.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
