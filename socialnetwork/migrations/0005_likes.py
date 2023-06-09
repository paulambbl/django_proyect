# Generated by Django 4.2.1 on 2023-06-06 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialnetwork', '0004_remove_post_dislikes_remove_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_from_user', to=settings.AUTH_USER_MODEL)),
                ('to_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_to', to='socialnetwork.post')),
            ],
        ),
    ]
