# Generated by Django 3.2.3 on 2021-05-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projcts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
