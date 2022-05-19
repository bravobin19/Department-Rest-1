from audioop import reverse
from django.db import models
from home.models import department

# Create your models here.


class employees(models.Model):
    employees_id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(
        department, default=None, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=False)
    age = models.DateTimeField(null=True)
    avatar = models.ImageField(upload_to='images', default=None)
    cv = models.FileField(upload_to='files', default=None)


def __str__(self):
    return f"{self.employees_id},{self.department_id},{self.name},{self.age},{self.avatar},{self.cv}"


def get_absolute_url(self):
    return reverse('department', args=[str(self.id)])

