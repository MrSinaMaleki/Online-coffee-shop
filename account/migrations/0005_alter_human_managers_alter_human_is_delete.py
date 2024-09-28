

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_merge_20240926_1409'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='human',
            managers=[
                ('activated', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='human',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
