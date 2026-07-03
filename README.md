# Contact Management App

A simple Django-based contact manager that stores contacts in a CSV file.

## Features
- Add a new contact with name and phone number
- View all saved contacts
- Update an existing contact
- Delete a contact with confirmation popup
- Prevent duplicate phone numbers
- Light/dark theme toggle
- Contacts persist in a CSV file and reload automatically on restart

## Requirements
- Python 3
- Django

## How to Run
1. Open the project folder:
   ```bash
   cd contactManagement
   ```
2. Install dependencies:
   ```bash
   pip install django
   ```
3. Start the server:
   ```bash
   python manage.py runserver
   ```
4. Open the app in your browser:
   ```text
   http://127.0.0.1:8000/managecontacts
   ```

## Notes
- The contacts are stored in a file named `contacts.csv` in the project root.
- If you want to run tests:
  ```bash
  python manage.py test
  ```
