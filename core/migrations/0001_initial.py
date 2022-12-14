# Generated by Django 4.1.3 on 2022-11-15 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventMetherologic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=200, null=True, verbose_name='position name')),
                ('details', models.CharField(max_length=250, null=True, verbose_name='details of event')),
                ('where', models.DateTimeField(auto_now_add=True, null=True, verbose_name='how event')),
                ('position', models.IntegerField(unique=True, verbose_name='position in graphic')),
            ],
        ),
    ]
