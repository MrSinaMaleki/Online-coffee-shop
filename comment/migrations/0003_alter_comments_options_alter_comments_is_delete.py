
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comments_reply_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
