from django.db import models

class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comentario #{}'.format(self.id)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=13)
    date_birth = models.DateField()
    document = models.FileField(upload_to="uploads/contact", default=None, null=True)

class TypeContact(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name