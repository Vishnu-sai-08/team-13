# Generated by Django 5.0.6 on 2024-06-22 06:09
from django.db import migrations, models
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('Username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=10)),
            ],
        ),
    ]
