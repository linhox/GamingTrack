# Generated by Django 3.1.1 on 2020-10-25 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamimgTrack', '0003_auto_20201023_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePostagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GamimgTrack.postagem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GamimgTrack.user')),
            ],
        ),
    ]
