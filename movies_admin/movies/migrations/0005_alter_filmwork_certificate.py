# Generated by Django 3.2 on 2023-02-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='certificate',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='certificate'),
        ),
    ]