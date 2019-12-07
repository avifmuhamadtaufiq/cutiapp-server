# Generated by Django 2.2.7 on 2019-12-02 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuti', '0004_auto_20191202_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='no_surat',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surats', to=settings.AUTH_USER_MODEL),
        ),
    ]
