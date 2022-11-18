from django.db import models
from django.urls import reverse

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Goat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)  

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'goat_id': self.id})


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  goat = models.ForeignKey(Goat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']