import requests
import string
import random


print("Discord Nitro Generator")
num = int(input('Enter the number of codes you want to generate'))


with open("Nitro Codes.txt", encoding='utf-8') as file:
    print("Codes are being generated, please wait")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code})

    print("Generated {num} codes")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("")

        url = "https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("Valid | {nitro}")  lines for
        else:
            print(f"*", end = "")   

print("The codes were generated")
