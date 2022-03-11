from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=250)
    city = forms.CharField(max_length=100)
    town = forms.CharField(max_length=100)
    email = forms.EmailField()
