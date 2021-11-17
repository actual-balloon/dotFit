from django.db import models

# Create your models here.
class Journal(models.Model):
    JOURNAL_TYPES = (
        ('Nutrition','Nutrition'),
        ('Exercise', 'Exercise')
    )
    name = models.CharField(max_length=60)
    journalType = models.CharField(max_length=9, choices=JOURNAL_TYPES)

    def _str_(self):
        return self.name

class Food(models.Model):
    food_name = models.CharField(max_length=60)
    unit_of_measurement = models.CharField(max_length=60)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    sugar = models.IntegerField()

    def _str_(self):
        return self.food_name

class JournalEntry(models.Model):
    entry_date = models.DateTimeField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)

    def _str_(self):
        return self.entry_date
