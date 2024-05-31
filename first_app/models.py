from django.db import models
from django.contrib.auth.models import  User
from django.db import models


# Create your models here.
class Post(models.Model):
    outher=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/"+str(self.id)+"/"

   #class Meta():
    # ordening=['-id']
    class MyModel(models.Model):
        # ... your model fields here

        class Meta:
            ordering = ['field1', '-field2']  # Order by field1 ascending, field2 descending

