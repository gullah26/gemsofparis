from django import forms


class EmailForm(forms.Form):  # email to collect email data from user
    email = forms.EmailField(label='Email', max_length=128)