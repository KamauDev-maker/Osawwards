# Generated by Django 4.0.5 on 2022-06-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='default.png', upload_to='post_images'),
        ),
    ]