# Generated by Django 3.2 on 2021-04-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssafy5_3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='webex_img',
            field=models.ImageField(upload_to='webex/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_img',
            field=models.ImageField(upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='webex_img',
            field=models.ImageField(upload_to='webex/'),
        ),
    ]
