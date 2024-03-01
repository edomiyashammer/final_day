# products/forms.py
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap form-control class to each form field widget
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap form-control class to each form field widget
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class SubmitForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(max_length=50)
    product_type = forms.CharField(max_length=50)
    quantite = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    information = forms.CharField(widget=forms.Textarea)
    review = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    image1 = forms.ImageField()
    location = forms.CharField(max_length=100)
    videolink = forms.URLField()
    sizes = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap form-control class to each form field widget
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'bg-gray-200 appearance-none border-2 border-gray-400 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'bg-gray-200 appearance-none border-2 border-gray-400 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'}))
