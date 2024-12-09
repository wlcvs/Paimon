from django.db import models
from django.core.exceptions import ValidationError

class Matriz(models.Model):
    name = models.CharField(max_length=200)
    num_of_lines_m = models.IntegerField(default=0)
    num_of_columns_n = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Element(models.Model):
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    # value
    line = models.IntegerField(default=0)
    column = models.IntegerField(default=0)

    def element_is_within_limits(self):
        if self.line > self.matriz.num_of_lines_m or self.column > self.matriz.num_of_columns_n:
            raise ValidationError("The element is outside the bounds of the matriz")

    def save(self, *args, **kwargs):
        self.element_is_within_limits()
        super().save(*args, **kwargs)
