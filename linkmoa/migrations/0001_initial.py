# Generated by Django 2.2.4 on 2019-08-08 23:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('owner', models.CharField(default='???', max_length=20)),
                ('directory', models.CharField(default='recently', max_length=20)),
                ('shared', models.BooleanField(default=False)),
                ('download', models.IntegerField(default=0)),
                ('keyword', models.CharField(max_length=30)),
                ('urls', models.TextField(default=None)),
                ('memo', models.TextField(default='')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 8, 8, 23, 26, 52, 548047), verbose_name='date_published')),
                ('tag', tagging.fields.TagField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numofDir', models.IntegerField(default=0)),
                ('selectedMemo', models.IntegerField(default=0)),
                ('currentdir', models.CharField(default='recently', max_length=20)),
                ('dir1', models.CharField(blank=True, max_length=30)),
                ('dir2', models.CharField(blank=True, max_length=30)),
                ('dir3', models.CharField(blank=True, max_length=30)),
                ('dir4', models.CharField(blank=True, max_length=30)),
                ('dir5', models.CharField(blank=True, max_length=30)),
                ('dir6', models.CharField(blank=True, max_length=30)),
                ('dir7', models.CharField(blank=True, max_length=30)),
                ('dir8', models.CharField(blank=True, max_length=30)),
                ('dir9', models.CharField(blank=True, max_length=30)),
                ('dir10', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
