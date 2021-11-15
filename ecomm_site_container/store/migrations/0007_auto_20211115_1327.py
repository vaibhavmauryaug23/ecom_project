# Generated by Django 3.2.8 on 2021-11-15 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211115_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='ecomuser',
            name='cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.cart'),
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('is_verified_buyer', models.BooleanField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ecomuser',
            name='wishlist',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.wishlist'),
            preserve_default=False,
        ),
    ]