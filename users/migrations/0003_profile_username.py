# Generated by Django 4.1.2 on 2022-10-31 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_created_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
