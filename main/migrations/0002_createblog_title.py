# Generated by Django 3.2.1 on 2021-05-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createblog',
            name='title',
            field=models.CharField(choices=[('django', 'Django'), ('html', 'HTML'), ('css', 'CSS')], default='djnago', max_length=7),
        ),
    ]
