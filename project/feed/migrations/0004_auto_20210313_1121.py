# Generated by Django 3.1.7 on 2021-03-13 11:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_review_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='rating_ambiance',
        ),
        migrations.AddField(
            model_name='review',
            name='rating_overall',
            field=models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rating_service',
            field=models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rating_taste',
            field=models.IntegerField(default=4, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
