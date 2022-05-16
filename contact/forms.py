from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import ContactForm


# Create your forms here.

class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email_address', 'message']
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 5,
                                        'class': "inputcontent"}),
            'first_name': TextInput(attrs={
                            'class': "inputcontent",
                            'placeholder': 'First Name'
                            }),
            'last_name': TextInput(attrs={
                            'class': "inputcontent",
                            'placeholder': 'Last Name'
                            }),
            'email_address': EmailInput(attrs={
                            'class': "inputcontent",
                            'placeholder': 'Email'
                            })
        }


