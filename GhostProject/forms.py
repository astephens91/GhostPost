from django import forms


class AddPost(forms.Form):
    is_boast = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'Roast'), (True, 'Boast')),
                   widget=forms.RadioSelect
                )
    content = forms.CharField(max_length=280)
    author = forms.CharField(max_length=20)
