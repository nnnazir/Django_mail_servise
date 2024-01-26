
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('mailing', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='client_to_message',
            field=models.ManyToManyField(related_name='client_to_message', to='client.mailingclient', verbose_name='Клиенты'),
        ),
    ]
