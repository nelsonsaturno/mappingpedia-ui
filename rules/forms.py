from django import forms


class UpdateRulesForm(forms.Form):

    name = forms.CharField(label="Name", help_text='Ex: Nelson')
    last_name = forms.CharField(label="Last name", help_text='Ex: Saturno')
    organization = forms.CharField(
        label="Organization",
        help_text='Ex: Ontology Engineering Group'
    )
    file = forms.FileField(label="Your file", help_text='No file selected.')
    description = forms.CharField(
        label="Rules description",
        widget=forms.Textarea,
        help_text='Enter your description here.'
    )
