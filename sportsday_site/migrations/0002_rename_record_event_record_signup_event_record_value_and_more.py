# Generated by Django 4.2.7 on 2024-02-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsday_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='record',
            new_name='record_signup',
        ),
        migrations.AddField(
            model_name='event',
            name='record_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Mixed')], max_length=1),
        ),
    ]