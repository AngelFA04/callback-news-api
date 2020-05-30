# Generated by Django 3.0.6 on 2020-05-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0004_auto_20200526_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='feed_type',
            field=models.CharField(choices=[('rss1', 'RSS1'), ('rss2', 'RSS2'), ('atom', 'ATOM'), ('html', 'HTML'), ('json', 'JSON')], default='rss2', max_length=4),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=200, verbose_name='source name'),
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.CharField(max_length=2048, verbose_name='source url'),
        ),
    ]
