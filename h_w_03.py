def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try: 
        name, phone = args
    except ValueError:
        return "Wrong input"
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    try: 
        name, phone = args
    except ValueError:
        return "Wrong input"
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    return "Contact is not found"

def phone_username(args, contacts):
    try: 
        name = args[0]
    except ValueError:
        return "Wrong input"
    if name in contacts:
        return contacts[name]
    return "Contact is not found"

def show_all_phones(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)


        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(show_all_phones(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
