contacts={}
while True:
    print('\nCONTACT BOOK APP')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contact')
    print('7. Exit')

    choice =input('Enter Your Choice: ')
    if choice =='1':
        name =input('Enter your name: ').title()
        if name in contacts:
            print(f'contact name{name} already exits (: ')
        else:
            age = input('Enter your age: ')
            email =input('Enter your email: ')
            mobile = input('Enter your mobile: ')
            contacts[name]={'age':int(age),'email':email,'mobile':mobile}
            print(f'contact name {name} added in application' )
    elif choice == '2':
        name =input('Enter contact name to view: ').title()
        if name in contacts:
            contact=contacts[name]
            print(f'Name : {name}, Age: {age}, Email: {email}, mobile: {mobile}')
        else:
            print('Contact not found')
    elif choice == '3':
        name=input('Enter the name you want to update detail: ').title()
        if name in contacts:
            age =input('Enter age : ')
            email=input('Enter new email: ')
            mobile=input('Enter new Mobile: ')
            contacts[name]={'age':int(age),'email':email,'mobile':mobile} 
            print(f'{name} profile have been updated')
        else:
            print(" Contact not found")
    elif choice =='4':
        name = input('enter the contact you want to delete: ').title()
        if name in contacts:
            del contacts[name]
            print(f'contact {name} has been delated')
        else:
            print('this contact not in app')
    elif choice =='5':
        name=input('Enter the contact name u want to search: ').title()
        if name in contacts:
            searched= contacts[name]
            print(f'the details of {name } is {searched}')
        else:
            print('Contact not found')
    elif choice =='6':
        print(f'The total contacts in book is : {len(contacts)}')
    elif choice == '7':
        print('Thank you for using Application')
        break
    else:
        print('Please Select correct choice ')
