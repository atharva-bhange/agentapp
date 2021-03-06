# Generated by Django 3.0.7 on 2020-06-23 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0006_auto_20200623_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(blank=True, max_length=20, null=True)),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='agent_role',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.Agents'),
        ),
        migrations.AlterField(
            model_name='agent_role',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agents.Roles'),
        ),
    ]
