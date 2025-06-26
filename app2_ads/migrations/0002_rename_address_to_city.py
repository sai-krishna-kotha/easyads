from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('app2_ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='address',
            new_name='city',
        ),
    ]
