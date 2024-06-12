from django import forms

TOPICS = (
    ('aa','AAA'),   # varname, display name
    ('bb','BBB'),
    ('cc','CCC'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPICS)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)
