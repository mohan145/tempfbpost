# Generated by Django 2.2.3 on 2019-07-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
