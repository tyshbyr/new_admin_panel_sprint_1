from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_updated_filmwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(
                choices=[
                    ('movie',
                     'Movie'),
                    ('tv_show',
                     'TV Show')],
                max_length=7,
                verbose_name='Type'),
        ),
    ]
