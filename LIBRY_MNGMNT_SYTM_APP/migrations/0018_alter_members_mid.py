# Generated by Django 3.2.15 on 2022-10-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIBRY_MNGMNT_SYTM_APP', '0017_issue_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='MID',
            field=models.TextField(blank=True),
        ),
    ]