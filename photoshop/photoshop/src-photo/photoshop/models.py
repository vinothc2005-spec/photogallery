from django.db import models


# REGISTER MODEL

class Register(models.Model):

    username = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# PHOTO MODEL

class Photo(models.Model):

    CATEGORY_CHOICES = (

        ('graphic', 'Graphic'),

        ('photoshop', 'Photoshop'),

        ('design', 'Design'),

    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(upload_to='photos/')

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title