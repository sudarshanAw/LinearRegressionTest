from django import forms

class Customer_Form(forms.Form):
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' : 'Enter your work experience in years'}))