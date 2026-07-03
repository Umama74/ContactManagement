import os
import tempfile
from pathlib import Path

from django.test import SimpleTestCase

from contact import storage


class ContactStorageTests(SimpleTestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.temp_file = self.temp_dir / 'contacts.csv'
        self.previous_path = os.environ.get('CONTACTS_CSV')
        os.environ['CONTACTS_CSV'] = str(self.temp_file)

    def tearDown(self):
        if self.previous_path is None:
            os.environ.pop('CONTACTS_CSV', None)
        else:
            os.environ['CONTACTS_CSV'] = self.previous_path

    def test_add_and_load_contacts(self):
        storage.add_contact('Alice', '1234567890')

        contacts = storage.load_contacts()

        self.assertEqual(contacts, [{'name': 'Alice', 'phone': '1234567890'}])

    def test_update_and_delete_contact(self):
        storage.add_contact('Bob', '5551234')
        storage.update_contact(0, 'Robert', '5559999')

        updated_contacts = storage.load_contacts()
        self.assertEqual(updated_contacts, [{'name': 'Robert', 'phone': '5559999'}])

        storage.delete_contact(0)
        self.assertEqual(storage.load_contacts(), [])

    def test_duplicate_phone_is_rejected_for_a_new_contact(self):
        storage.add_contact('Alice', '1234567890')

        with self.assertRaises(ValueError):
            storage.add_contact('Bob', '1234567890')
