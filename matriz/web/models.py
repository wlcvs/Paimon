from django.db import models
from django.core.exceptions import ValidationError

class Matriz(models.Model):
    name = models.CharField(max_length=200, null=True)
    num_of_lines_m = models.IntegerField()
    num_of_columns_n = models.IntegerField()

    def __str__(self):
        return self.name

class Element(models.Model):
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    value = models.FloatField()
    line = models.IntegerField()
    column = models.IntegerField()

    def element_is_within_limits(self):
        if self.line > self.matriz.num_of_lines_m or self.column > self.matriz.num_of_columns_n:
            raise ValidationError("The element is outside the bounds of the matriz")
        else:
            return True

    # Verifica se não há nenhum elemento na posição em questão
    def there_is_no_element_in_this_position_yet(self):
        if not (Matriz.objects.filter(line__exact = self.line).exists()) and not (Matriz.objects.filter(column__exact = self.column).exists()):
            return True
        else:
            raise ValidationError(f"There is already an element in row {self.line} and column {self.column}")

    def save(self, *args, **kwargs):
        if self.element_is_within_limits() and self.there_is_already_an_element_in_this_position():
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Value {self.value} in the matriz {self.matriz.name} in row {self.line} and column {self.column}"
