# Generated by Django 3.1.4 on 2021-05-06 08:42


import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/ytubers/%Y/%m')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)) ,
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255)),
                ('camera_type', models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('sony', 'sony'), ('red', 'red'), ('fuji', 'fuji'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=255)),
                ('sub_count', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('flim_makinhg', 'film_making'), ('cooking', 'cooking')], max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
