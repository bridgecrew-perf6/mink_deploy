# Generated by Django 4.0.1 on 2022-03-10 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summernote_support', '0002_rename_summernote_abstractattachment_attachment_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attachment',
            new_name='mink_Attachment',
        ),
    ]
