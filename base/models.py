from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tbTodo(models.Model):
    tdUser = models.ForeignKey(User, on_delete=models.CASCADE)
    tdName =models.CharField(max_length=50)
    tdDes = models.TextField(null=True , blank=True)
    tdStatus = models.BooleanField(default=False)
    tdIsDeleted = models.BooleanField(default= False)
    tdDate = models.DateTimeField(auto_now_add=True)


    # official name 
    def __str__(self):
        return self.tdName
    
class  Meta:
    ordiering = ['tdStatus']
