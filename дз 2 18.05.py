користувачі = {
    'Максим': 13,
    'Єва': 12,
    'Андрій': 14
}
ім_я = input("Будь ласка, введіть ім'я користувача: ")
if ім_я in користувачі:
    print(f"Вік користувача {ім_я}: {користувачі[ім_я]} років.")
else:
    print("Користувача з таким ім'ям не знайдено у словнику.")
