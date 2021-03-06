# Generated by Django 2.0.1 on 2018-02-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trump', '0002_cnn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=100)),
                ('followers_count', models.IntegerField()),
                ('friends_count', models.IntegerField()),
                ('statuses_count', models.IntegerField()),
                ('favourites_count', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wikipedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=100)),
                ('page_url', models.CharField(max_length=100)),
                ('page_summary', models.CharField(max_length=200)),
                ('page_content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Trump',
        ),
    ]
