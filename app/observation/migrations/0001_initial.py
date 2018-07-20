# Generated by Django 2.0.7 on 2018-07-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('recorded_at', models.DateTimeField(unique=True)),
            ],
            options={
                'ordering': ('-recorded_at',),
            },
        ),
    ]