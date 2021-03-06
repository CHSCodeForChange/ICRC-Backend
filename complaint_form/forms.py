from django import forms
from .models import *

class PlaceholderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.EmailInput, forms.NumberInput, forms.DateInput):
                    field.widget.attrs.update(
                        {'placeholder': field.label, 'class': 'span10 form-control'}
                    )
                if type(field.widget) is (forms.DateInput):
                    field.widget.attrs.update(
                        {'placeholder': field.label + " (mm/dd/yyyy)", 'class': 'span10 form-control'}
                    )
                if type(field.widget) in (forms.Select, ):
                    field.widget.attrs.update({'placeholder': field.label, 'class': 'span10'})
                    field.choices = [("", field.label),] + list(field.choices)[1:] 
                    field.empty_label = field.label

    def as_p(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True
        )


class DateInput(forms.DateInput):
    input_type = 'date'


class NewComplaintForm(PlaceholderForm):
    discrimination_description = forms.CharField(widget=forms.Textarea(attrs={'type': 'text',
           'class': 'form-control',
           'rows':10,
           'cols':58}))
    class Meta:
        model = Complaint
        exclude = []
