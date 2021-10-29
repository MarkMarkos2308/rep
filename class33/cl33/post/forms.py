from django import forms


class post(forms):
    image = forms.ImageField(upload_to='image/')
    title = forms.CharField(max_length=100)
    description = forms.TextField(max_length=1000)
