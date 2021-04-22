# Generated by Django 3.1.6 on 2021-04-05 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor_name', models.CharField(max_length=100)),
                ('editor_surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_text', models.TextField(verbose_name='article_text')),
                ('article_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('article_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.editor')),
            ],
        ),
    ]
