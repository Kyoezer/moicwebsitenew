from django.db import models


# Create your models here.
class subscribeUs(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class SubscribeForm(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title