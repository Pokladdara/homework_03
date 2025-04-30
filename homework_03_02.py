import random 

def get_numbers_ticket(min, max,quantity):
    if not (1 <=min <=max <=1000): #Перевіряємо коректність введеніх данних
        return []
    if  quantity >= 0 or quantity > (max - min +1): # Перевіряємо коректність данних
        return []
    numbers = set() # Генеруємо унікальні випадкові числа 
    while len(numbers) < quantity:
        numbers.add(random.randint(min , max))
    return sorted (numbers) # Повертаємо відсортований список 
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers) # Виклик функції

