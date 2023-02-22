# Generated by Django 2.2.13 on 2020-06-30 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200515_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.ContentProvider')),
            ],
        ),
    ]