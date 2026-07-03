from django.shortcuts import redirect, render

from . import storage


def manage_contacts(request):
    contacts = storage.load_contacts()
    action = request.GET.get('action', 'view')
    selected_index = request.GET.get('index')
    selected_contact = None

    if selected_index is not None:
        try:
            selected_index = int(selected_index)
            selected_contact = contacts[selected_index]
        except (ValueError, IndexError):
            selected_contact = None

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        contact_id = request.POST.get('contact_id')
        action_name = request.POST.get('action', 'view')

        if action_name == 'delete' and contact_id is not None:
            storage.delete_contact(int(contact_id))
            return redirect('manage_contacts')

        if not name or not phone:
            return render(request, 'contact/manage_contacts.html', {
                'contacts': contacts,
                'error': 'Name and contact number are required.',
                'action': action_name,
                'selected_contact': selected_contact,
                'selected_index': selected_index,
            })

        try:
            if action_name == 'update' and contact_id is not None:
                storage.update_contact(int(contact_id), name, phone)
            else:
                storage.add_contact(name, phone)
        except ValueError as exc:
            return render(request, 'contact/manage_contacts.html', {
                'contacts': contacts,
                'error': str(exc),
                'action': action_name,
                'selected_contact': selected_contact,
                'selected_index': selected_index,
            })

        return redirect('manage_contacts')

    return render(request, 'contact/manage_contacts.html', {
        'contacts': contacts,
        'action': action,
        'selected_contact': selected_contact,
        'selected_index': selected_index,
    })
