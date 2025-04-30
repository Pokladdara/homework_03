import re

phone = ('067\t123 4567')

def normalize_phone(phone):
    cleaned_number = re.sub(r'[^0-9]' , ''  , phone) #Прибираемо всі символи окрім цифр 
    if cleaned_number.startswith('380'): # Перевіряємо починается з 380
        cleaned_number = '+' + cleaned_number
    else:
        cleaned_number = '+38' + cleaned_number # Додаємо +38 до номерів в які починаются з 0
    return cleaned_number
           
print("Нормалізований номер телефону для SMS-розсилки:", normalize_phone(phone)) #Виклик функції
