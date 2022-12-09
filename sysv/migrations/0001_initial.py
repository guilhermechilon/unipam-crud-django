from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('preco', models.CharField(max_length=30)),
                ('imagem', models.ImageField(upload_to='')),
                ('descriao', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=160)),
            ],
        ),
    ]
