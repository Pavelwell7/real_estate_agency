import phonenumbers

from django.db import migrations

def normalize_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for number in Flat.objects.all():
        raw_number = number.owners_phone_number
        if raw_number:
            parsed_number = phonenumbers.parse(raw_number, 'RU')
            if phonenumbers.is_valid_number(parsed_number):
                number.owner_pure_phone = parsed_number
                number.save()


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
