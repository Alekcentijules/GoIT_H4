"""Module with command processing functions."""

def add_contact(args, contacts):
    """
    Adds a new contact.

    Args:
        args (List[str]): List of arguments: [name, phone]
        contacts (Dict[str, str]): Dictionary of contacts

    Returns:
        str: Message about the result
    """
    if len(args) != 2:
        return "Add requires name and phone."
    name, phone = args
    if not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    elif name in contacts:
        return "This contact was add."
    contacts[name] = phone
    return "Contact added!"

def change_contact(args, contacts):
    """
    Changes the number of an existing contact.

    Args:
        args (List[str]): [name, new_number]
        contacts (Dict[str, str]): Dictionary of contacts

    Returns:
        str: Message about the result
    """
    if len(args) != 2:
        return "Change requires name and new phone."
    name, phone = args
    if name not in contacts:
        return "This contact isn't in list."
    elif not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    contacts[name] = phone
    return "Contact changed!"

def output_phone(args, contacts):
    """
    Displays the phone number by name.

    Args:
        args (List[str]): [name]
        contacts (Dict[str, str]): Contact dictionary

    Returns:
        str: Phone number or error message
    """
    if len(args) != 1:
        return "Phone requires exactly one name."
    name = args[0]
    if name not in contacts:
        return "This contact isn't in list."
    return contacts[name]
