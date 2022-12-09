from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='codigo',
            field=models.CharField(max_length=100),
        ),
    ]
