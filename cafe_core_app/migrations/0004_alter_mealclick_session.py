# Generated by Django 4.1.4 on 2022-12-25 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('cafe_core_app', '0003_mealclick_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealclick',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.session'),
        ),
    ]