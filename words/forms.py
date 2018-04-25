from dal import autocomplete
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML

from crispy_forms.layout import Submit

from .models import *


class AbbreviationFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AbbreviationFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'orth',
                'expanded',
                'lemma',
                'pos',
                css_id="basic_search_fields"
                ),
            )


class AbbreviationForm(forms.ModelForm):
    class Meta:
        model = Abbreviation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AbbreviationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
