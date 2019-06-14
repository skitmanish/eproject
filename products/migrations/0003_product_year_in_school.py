# Generated by Django 2.1.5 on 2019-06-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190610_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR ', 'Junior'), ('SR ', 'Senior')], default='FR', max_length=2),
        ),
    ]
