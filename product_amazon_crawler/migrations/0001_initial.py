# Generated by Django 4.1.13 on 2024-06-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonDataScrapCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=20)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
