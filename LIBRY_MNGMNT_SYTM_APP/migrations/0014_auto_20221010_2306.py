# Generated by Django 3.2.15 on 2022-10-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIBRY_MNGMNT_SYTM_APP', '0013_auto_20221010_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='penalty',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='penalty',
        ),
    ]
