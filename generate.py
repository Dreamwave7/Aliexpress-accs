import json
import faker
import random
import pprint

fake = faker.Faker()


def generate_emails(value):
    base = []
    basic_url= "rus.emailfake.com/"
    for i in range(value):
        name = fake.name().replace(" ","")+str(random.randint(1,999))
        link = f"{basic_url}{name}@traz.cc".lower()
        email = f"{name}@traz.cc".lower()
        account = {
            "Почта": email,
            "Пароль": fake.password(),
            "Ссылка": link,
            "Товар":"None"
            }
        base.append(account)
    return base
        

def email_to_txt():
    separator = "============================="
    with open("accs.txt","w",encoding="utf-8") as file:
        accounts = generate_emails(100)
        for acc in accounts:
            text = (f'''
\n{separator}\n
Почта: {acc["Почта"]}\n
Пароль: {acc["Пароль"]}\n
Ссылка: {acc["Ссылка"]}\n
Товар: {acc["Товар"]}\n
''')
            file.write(text)
if __name__=="__main__":
    email_to_txt()

