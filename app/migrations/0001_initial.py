# Generated by Django 2.2.4 on 2019-08-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=109)),
                ('photo', models.ImageField(upload_to='users/')),
            ],
        ),
    ]
