# Generated by Django 2.2.7 on 2019-12-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuti', '0005_auto_20191202_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='no_surat',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
