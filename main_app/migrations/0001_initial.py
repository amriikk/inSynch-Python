from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=100)),
                ('band', models.CharField(max_length=100)),
                ('mood', models.CharField(choices=[('A', 'Angry'), ('B', 'Melancholy'), ('C', 'Cheerful'), ('D', 'Calm'), ('E', 'Romantic'), ('F', 'Mysterious')], default='A', max_length=1)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
