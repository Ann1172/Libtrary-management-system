# Generated by Django 3.2.15 on 2022-10-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIBRY_MNGMNT_SYTM_APP', '0006_auto_20221003_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]