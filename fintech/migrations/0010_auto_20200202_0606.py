# Generated by Django 3.0.2 on 2020-02-02 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fintech', '0009_auto_20200202_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_idea11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('domain', models.TextField(max_length=200)),
                ('ncollab', models.IntegerField()),
                ('link', models.TextField(max_length=300)),
                ('about', models.TextField(max_length=1000)),
                ('nlike', models.IntegerField()),
                ('nviews', models.IntegerField()),
                ('email', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='watchlist1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.TextField(max_length=200)),
                ('title', models.TextField(max_length=200)),
                ('email', models.TextField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='register_investor1',
            new_name='register_investor11',
        ),
        migrations.RenameModel(
            old_name='register_user1',
            new_name='register_user11',
        ),
        migrations.RenameModel(
            old_name='user_profile1',
            new_name='user_profile11',
        ),
        migrations.DeleteModel(
            name='add_idea1',
        ),
    ]
