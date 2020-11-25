from django import forms
class Add_item_form(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
