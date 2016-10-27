import django.forms as forms


class MemoForm(forms.Form):
    username = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
