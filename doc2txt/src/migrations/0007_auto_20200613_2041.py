# Generated by Django 3.0.7 on 2020-06-13 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_auto_20200613_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='ques_img_blank',
            new_name='ques_image',
        ),
    ]
