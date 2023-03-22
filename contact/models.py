from django.db import models

class Contact(models.Model):
    """
    Contact model, i want to save all contact form submisions in database. 
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    sent_message = models.CharField(max_length=10000)
    sent_date = models.DateField(auto_now_add=True)
    sent_time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_date']

    def __str__(self):
        return self.email