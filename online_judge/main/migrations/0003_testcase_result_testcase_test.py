# Generated by Django 4.2.3 on 2023-07-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_testcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='result',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testcase',
            name='test',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
