# Generated by Django 2.0.7 on 2019-06-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20190609_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='department',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
    ]
