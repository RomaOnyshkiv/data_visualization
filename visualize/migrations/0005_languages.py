# Generated by Django 2.2.3 on 2019-07-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0004_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
    ]
