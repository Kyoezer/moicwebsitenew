from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import SubscribeForm, MailMessage, subscribeUs
from django import forms


# Create your forms here.

# class SubscribeForm(ModelForm):
#     class Meta:
#         model = SubscribeForm
#         fields = ['name',  'email_address']
#         widgets = {
#             'message': Textarea(attrs={'cols': 30, 'rows': 5,
#                                         'class': "inputcontent"}),
#             'name': TextInput(attrs={
#                             'class': "inputcontent",
#                             'placeholder': 'Name'
#                             }),

#             'email_address': EmailInput(attrs={
#                             'class': "inputcontent",
#                             'placeholder': 'Email'
#                             })
#         }


class SubscribeForm(ModelForm):
    class Meta:
        model = subscribeUs
        fields = ['email', ]
        widgets = {
        'email': EmailInput(attrs={
                            'class': "inputcontent",
                            'placeholder': 'Email'
                            })
        }


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'

