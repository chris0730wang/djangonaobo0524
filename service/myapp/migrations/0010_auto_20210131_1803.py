# Generated by Django 3.1.1 on 2021-01-31 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210129_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='U7BeforeYouReadAns',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('unit', models.CharField(max_length=2)),
                ('number', models.IntegerField()),
                ('numofchoose1', models.IntegerField()),
                ('numofchoose2', models.IntegerField()),
                ('numofchoose3', models.IntegerField()),
                ('numofchoose4', models.IntegerField()),
                ('numofchoose5', models.IntegerField()),
                ('totalchoose', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='BeforeYouReadAns',
            new_name='U5BeforeYouReadAns',
        ),
    ]