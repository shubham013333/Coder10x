# Generated by Django 5.1 on 2024-09-15 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0003_subscriber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscriber',
            new_name='Subscription',
        ),
    ]
