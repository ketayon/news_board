# Generated by Django 3.0.7 on 2020-06-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
