# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 20:06
from __future__ import unicode_literals

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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='about company')),
                ('location', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('total_job_posted', models.IntegerField(default=0)),
                ('company_website', models.URLField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('vacancy', models.IntegerField()),
                ('job_nature', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('job_requirement', models.TextField()),
                ('educational_requirement', models.CharField(max_length=200)),
                ('experience_needed', models.IntegerField()),
                ('age_range', models.CharField(max_length=50)),
                ('job_location', models.CharField(max_length=200)),
                ('salary_range', models.CharField(max_length=50)),
                ('apply_instruction', models.TextField()),
                ('job_posted_date', models.DateField(auto_now_add=True)),
                ('job_deadline', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Company')),
            ],
        ),
    ]