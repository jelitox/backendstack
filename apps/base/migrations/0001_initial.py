# Generated by Django 2.1 on 2018-08-04 13:36

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
            name='AcademicLevel',
            fields=[
                ('name', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='Academic Name')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='Description')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'Academic Level',
                'verbose_name_plural': 'Academics Levels',
                'db_table': 'base_academic',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='City')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'db_table': 'base_cities',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Country Name')),
                ('country_code', models.CharField(default='US', max_length=2, verbose_name='Country Code')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'db_table': 'base_countries',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('last_update', models.DateTimeField(auto_now_add=True, verbose_name='Last update')),
                ('píc', models.ImageField(blank=True, null=True, upload_to='static/images/profiles/')),
                ('address', models.CharField(max_length=120, null=True, verbose_name='Address')),
                ('enabled', models.BooleanField(default=True)),
                ('academic_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.AcademicLevel')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Cities')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Countries')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'db_table': 'base_user_profile',
            },
        ),
        migrations.AddField(
            model_name='cities',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Countries', verbose_name='Country'),
        ),
    ]