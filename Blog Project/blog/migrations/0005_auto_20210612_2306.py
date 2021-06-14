# Generated by Django 3.2.3 on 2021-06-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210612_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_posted',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
