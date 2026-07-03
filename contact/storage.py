import csv
import os
from pathlib import Path
from typing import List, Dict


def get_storage_path() -> Path:
    configured_path = os.environ.get('CONTACTS_CSV')
    if configured_path:
        return Path(configured_path)
    return Path(__file__).resolve().parent.parent / 'contacts.csv'


def load_contacts() -> List[Dict[str, str]]:
    path = get_storage_path()
    if not path.exists():
        return []

    with path.open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        return [{'name': row['name'], 'phone': row['phone']} for row in reader if row]


def save_contacts(contacts: List[Dict[str, str]]) -> None:
    path = get_storage_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=['name', 'phone'])
        writer.writeheader()
        writer.writerows(contacts)


def add_contact(name: str, phone: str) -> None:
    contacts = load_contacts()
    if any(contact['phone'] == phone for contact in contacts):
        raise ValueError('A contact with this phone number already exists.')
    contacts.append({'name': name, 'phone': phone})
    save_contacts(contacts)


def update_contact(index: int, name: str, phone: str) -> None:
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        for current_index, contact in enumerate(contacts):
            if current_index != index and contact['phone'] == phone:
                raise ValueError('A contact with this phone number already exists.')

        contacts[index] = {'name': name, 'phone': phone}
        save_contacts(contacts)


def delete_contact(index: int) -> None:
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
