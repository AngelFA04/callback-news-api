# Generated by Django 3.0.6 on 2020-05-25 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0002_auto_20200525_0746'),
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time when object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time when object last modified', verbose_name='modified at')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('description', models.TextField(null=True)),
                ('content', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('date_posted', models.CharField(max_length=50)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(default='001', null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('media', models.ForeignKey(default='001', null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Media')),
                ('user', models.ForeignKey(default='001', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
