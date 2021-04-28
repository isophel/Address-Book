'''
Address book:
Add contact
View contacts
Retrieve contact
Update contact
Delete contact
'''


# DEfine global storage data structure
contacts = []

# Get users option 
def address_book():
    action = input("\n Choose any of these options \n a: to add contact Add contact \n v: to view contacts \n r: to retrieve specific contact \n u: to update contact \n d: to delete a contact \n q: to quit ")

    while action != 'q':
        if action == 'a':
            add_contact()
        elif action == 'v':
            list_contacts()
        elif action == 'r':
            find_contact()
        elif action == 'u':
            update_contact() 
        elif action == 'd':
            delete_contact()        
        else:
            print("Invalid option, please try again!") 
        action = input("\n Choose any of these options \n a: to add contact Add contact \n v: to view contacts \n r: to retrieve specific contact \n u: to update contact \n d: to delete a contact \n q: to quit ")
    

# Create contact     
def add_contact():
    name=input("Enter name:")
    email=input("Enter email:")    
    telephone=input("Enter contact:") 
    # Append user input as dictionary to list
    contacts.append({
        'name': name,
        'email': email,
        'telephone': telephone,
    })
    print(f"You added name: {name}, email: {email} tel: {telephone}")


# Show contacts 
def list_contacts():
    if contacts != []:
        for contact in contacts:
            print(f"name: {contact['name']}")
            print(f"email: {contact['email']}")
            print(f"telephone: {contact['telephone']} \n")
    else:
        print("\n No contacts available")    


# Search for contact
""" Provide key to compare value with, return dictionary if dictionary exists """
def find_contact():
    filter_by = input("Property to find: ")
    if filter_by != "name" or filter_by != "email" or filter_by != "telephone":
        print("\n Please enter appropriate filter. \n Choices are name, email and telephone")
        filter_by = input("Property to find: ")
    look_for = input("Search for: ")
    found = []

    # append dictionary to empty list
    for contact in contacts:
        if contact[filter_by] == look_for:
            found.append(contact)
            print(found)
        # ele:
        #     print("\n Contsact not found")    
    return found  


# search for contact
""" Provide key to compare value with, return dictionary if dictionary exists """
def update_contact():
    filter_by = input("Property to find: ")
    # if filter_by != "name" or filter_by != "email" or filter_by != "telephone":
    #     print("\n Please enter appropriate filter. \n Choices are name, email and telephone")
    look_for = input("Search for: ")
    found = []

    for contact in contacts:
        if contact[filter_by] == look_for:
            found.append(contact)
            for_update=found[0]

            # delete dictionary
            index_of_contact = contacts.index(contact)
            del contacts[index_of_contact]

            # update
            name=input("Update name:")
            email=input("Update email:")    
            telephone=input("Update contact:") 

            for_update.update({
                'name': name,
                'email': email,
                'telephone': telephone,
            })

            print(f"You updated name: {for_update['name']} email: {for_update['name']} telephone: {for_update['name']}")
            # update contacts list
            contacts.append(for_update)
      
        else:
            print("\n Contact not found")    
    return for_update  


def delete_contact():
    filter_by = input("Property to filter with: ")
    if filter_by != "name" or filter_by != "email" or filter_by != "telephone":
        print("\n Please enter appropriate filter. \n Choices are name, email and telephone")
    look_for = input("Search for: ")
    look_for = input("Delete: ")
    found = []

    for contact in contacts:
        if contact[filter_by] == look_for:
            index_of_contact = contacts.index(contact)
            del contacts[index_of_contact]
        else:
            print("\n Contact not found")   

s="ice cream address"
# Write to html
f = open('address-website.html','w')

parse_script = f"""
<html>
<head></head>
<title>python script </title>
<body>
<p>Hello World!</p>
<p> {s} </p>
{contacts}
</body>
</html>
"""

f.write(parse_script)
f.close()                    

address_book() 
