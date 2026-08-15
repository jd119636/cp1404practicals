def main():
    email_to_name ={}
    email = input("email:")
    while email != "":
        name = find_name(email)
        confirmation =input(f"Is your name {name}? (Y/N) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name:")
        email_to_name[email] = name
        email = input("Email: ")

    for email in email_to_name:
        print(f"{email}: {email_to_name[email]}")

    for email, name in email_to_name.items():
        print(f"{email}: {name}")

def find_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()