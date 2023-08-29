# Generated by Django 3.2.20 on 2023-08-22 13:21

from django.db import migrations, models

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0048_version_4_6_3'),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "4.7.0", "The new version of the calendar allows users to view multiple tool feeds at once by checking the box next to each tool you would like to see.")

    operations = [
        migrations.RunPython(new_version_news),
        migrations.AddField(
            model_name='area',
            name='auto_logout_time',
            field=models.PositiveIntegerField(blank=True, help_text='Number of minutes after which users will be automatically logged out of this area.', null=True),
        ),
        migrations.AlterField(
            model_name='closure',
            name='staff_absent',
            field=models.BooleanField(default=True, help_text='Check this box and all staff members will be marked absent during this closure in staff status.', verbose_name='Staff absent entire day'),
        ),
    ]
