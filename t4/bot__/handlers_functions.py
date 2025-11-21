from .processor_functions import add_contact, change_contact, output_phone

def handler_add(args, contacts):    
    return add_contact(args, contacts)

def handler_change(args, contacts):
    return change_contact(args, contacts)

def handler_phone(args, contacts):
    return output_phone(args, contacts)

def handler_all(contacts):
    if not contacts:
        return 'No contacts saved.'
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

COMMANDS = {
    'hello': 'How can i help you?',
    'add': handler_add,
    'change': handler_change,
    'phone': handler_phone, 
    'all': handler_all,
    'close': 'Good bye!',
    'exit': 'Good bye!'

}
