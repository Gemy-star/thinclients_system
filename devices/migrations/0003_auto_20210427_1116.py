# Generated by Django 3.2 on 2021-04-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_thinunits_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='thinunits',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='thinunits',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
