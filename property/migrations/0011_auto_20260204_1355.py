import phonenumbers

from django.db import migrations

def normalize_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        raw_number = flat.owners_phone_number
        if raw_number:
            parsed_number = phonenumbers.parse(raw_number, 'RU')
            if phonenumbers.is_valid_number(parsed_number):
                flat.owner_pure_phone = parsed_number
                flat.save()


def move_backend(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone='')


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_alter_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_number, move_backend)
    ]
