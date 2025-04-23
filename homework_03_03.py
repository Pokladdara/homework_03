import re

phone_numbers = ["    +38(050)123-32-34",
                 "     0503451234",
                 "(050)8889900",
                 "38050-111-22-22",
                 "38050 111 22 11   "
                 ]
def normalize_phone(phone_numbers):
    for phone in phone_numbers:
        cleaned_number = re.sub(r'[^0-9]' , ''  , phone) #Прибираемо всі символи окрім цифр 
        if not cleaned_number.startswith('+'): # Перевіряемо починается номер з +
            if cleaned_number.startswith('380'): # Перевіряємо починается з 380
                cleaned_number = '+' + cleaned_number
            else:
                 cleaned_number = '+38' + cleaned_number # Додаємо +38 до номерів в які починаются з 0
                 return cleaned_number
           
print("Нормалізований номер телефону для SMS-розсилки:", normalize_phone(phone_numbers)) #Виклик функції
