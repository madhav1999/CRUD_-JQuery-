from django.db import models


class Sample(models.Model):
    Name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Name
