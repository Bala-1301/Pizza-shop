# Generated by Django 3.0.5 on 2020-06-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_auto_20200602_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplatter',
            name='largePrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='smallPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='extra',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5),
        ),
        migrations.AlterField(
            model_name='extracheese',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pastawithserving',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='largePrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='oneToppingLarge',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='oneToppingSmall',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='smallPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='specialLarge',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='specialSmall',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='threeToppingsLarge',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='threeToppingsSmall',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='twoToppingsLarge',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='twoToppingsSmall',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='salad',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sub',
            name='largePrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sub',
            name='smallPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]