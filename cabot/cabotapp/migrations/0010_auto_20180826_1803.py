# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-26 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabotapp', '0009_auto_20180731_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuscheck',
            name='json_schema',
            field=models.TextField(blank=True, help_text=b'JSON Schema against response body.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='body',
            field=models.TextField(blank=True, help_text=b'Request body in json format, Learn to write JSON <a href="https://en.wikipedia.org/wiki/JSON" target="_blank">here</a>. In case of GET request body is ignored.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='method',
            field=models.CharField(choices=[(b'get', b'GET'), (b'post', b'POST'), (b'put', b'PUT'), (b'delete', b'DELETE'), (b'patch', b'PATCH')], default=b'ge', help_text=b'Request method.', max_length=255),
        ),
    ]
