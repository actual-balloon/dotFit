# Generated by Django 3.2.9 on 2021-11-05 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=60)),
                ('unit_of_measurement', models.CharField(max_length=60)),
                ('calories', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('carbohydrates', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('sugar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('journalType', models.CharField(choices=[('Nutrition', 'Nutrition'), ('Exercise', 'Exercise')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField()),
                ('foods', models.ManyToManyField(to='journal.Food')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.journal')),
            ],
        ),
    ]