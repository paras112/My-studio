from django import forms
from .models import SignUp
class ContactForm(forms.Form):
	full_name=forms.CharField(required=False)
	email=forms.EmailField()
	message=forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=['full_name','email']

	def clean_email(self):
		email= self.cleaned_data.get('email')
		return email