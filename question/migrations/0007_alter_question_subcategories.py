# Generated by Django 3.2 on 2021-05-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210504_2326'),
        ('question', '0006_auto_20210505_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subcategories',
            field=models.ManyToManyField(to='quiz.SubCategory'),
        ),
    ]
