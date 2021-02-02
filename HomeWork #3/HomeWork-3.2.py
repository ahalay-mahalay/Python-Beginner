def print_user_data(name, surname, year, city, email, phone):
    print(f"{name} {surname}, {year}, {city}, {email}, {phone}")


print_user_data(name=input("Name: "),
                surname=input("Surname: "),
                year=input("Year of birth: "),
                city=input("City: "),
                email=input("email: "),
                phone=input("Phone number: "))
