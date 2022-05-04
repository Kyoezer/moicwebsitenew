from django.forms import ModelForm, Textarea
from .models import ContactForm


# Create your forms here.

class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 10}),
        }
        fields = '__all__'
