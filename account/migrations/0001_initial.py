# Generated by Django 5.1.1 on 2024-10-01 09:09

import account.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image', validators=[account.models.validate_image_size])),
            ],
            options={
                'verbose_name': 'Account USER',
                'verbose_name_plural': 'Account USERS',
                'ordering': ['-date_joined'],
            },
            bases=('auth.user', models.Model),
        ),
    ]
