from django.db import models
from django.core.exceptions import ValidationError

class Matriz(models.Model):
    name = models.CharField(max_length=200, null=True)
    num_of_lines_m = models.IntegerField(default=0)
    num_of_columns_n = models.IntegerField(default=0)

class Element(models.Model):
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    line = models.IntegerField(default=0)
    column = models.IntegerField(default=0)

    def element_is_within_limits(self):
        if self.line > self.matriz.num_of_lines_m or self.column > self.matriz.num_of_columns_n:
            raise ValidationError("The element is outside the bounds of the matriz")
        else:
            return True

<<<<<<< HEAD
    # Verificar se o elemento já nesta posição já existe na matriz em questão
    def there_is_already_an_element_in_this_position(self):
        if  Matriz.objects.filter(line__exact=self.line) or  Matriz.objects.filter(column__exact=self.column):
            raise ValidationError(f"There is already an element at this position in the matriz, line: {self.line}, column: {self.column}")
        else:
=======
    # Verifica se não há nenhum elemento na posição em questão
    def there_is_no_element_in_this_position_yet(self):
        if !(Matriz.objects.filter(line__exact = self.line).exists()) and !(Matriz.objects.filter(column__exact = self.column).exists()):
>>>>>>> 4104a10 (Pelo menos alguma coisa está sendo listada)
            return True
        else:
            raise ValidationError(f"There is already an element in row {self.line} and column {self.column}")

    def save(self, *args, **kwargs):
        if self.element_is_within_limits() and self.there_is_already_an_element_in_this_position():
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Value {self.value} in the matriz {self.matriz.name} in row {self.line} and column {self.column}"
