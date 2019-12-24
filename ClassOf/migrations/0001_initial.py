# Generated by Django 2.2.7 on 2019-12-24 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('dept_id', models.CharField(max_length=5)),
                ('dept_hod', models.CharField(max_length=25)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('school_address', models.CharField(max_length=50)),
                ('school_email', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('institution_head', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Graduate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('other_name', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('lga_of_origin', models.CharField(max_length=15)),
                ('state_of_origin', models.CharField(max_length=15)),
                ('fav_quote', models.TextField(blank=True, null=True)),
                ('admission_year', models.IntegerField()),
                ('best_experience', models.TextField(blank=True, null=True)),
                ('worst_experience', models.TextField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=25)),
                ('birth_day', models.DateField()),
                ('photo', models.ImageField(upload_to='Photos/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClassOf.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=60)),
                ('faculty_id', models.CharField(max_length=5)),
                ('faculty_deen', models.CharField(max_length=25)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClassOf.School')),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClassOf.Faculty'),
        ),
    ]
