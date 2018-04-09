# Generated by Django 2.0.3 on 2018-04-09 05:38

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocontext', '0008_auto_20180409_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextcache',
            name='geometry_3d',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, dim=3, help_text='The 3D geometry of the context.', null=True, srid=4326),
        ),
    ]
