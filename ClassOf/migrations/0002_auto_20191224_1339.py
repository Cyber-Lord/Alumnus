# Generated by Django 2.2.7 on 2019-12-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassOf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduate',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Prefer not to say')], default='M', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='motto',
            field=models.CharField(default='Hello', max_length=50),
            preserve_default=False,
        ),
    ]
