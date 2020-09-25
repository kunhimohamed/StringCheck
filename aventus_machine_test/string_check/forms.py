from django import forms

class SimpleForm(forms.Form):
		master_string = forms.CharField(
		    label='Master String'
		)
		string_1 = forms.CharField(
		    label='String 1'
		)
		string_2 = forms.CharField(
		    label='String 2'
		)
		string_3 = forms.CharField(
		    label='String 3'
		)
		string_4 = forms.CharField(
		    label='String 4'
		)