
from datetime import datetime

def get_days_from_today(date):
    try:
        requested_day = datetime.strptime(date, '%Y-%m-%d').date() #Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        today_date = datetime.today().date() #Отримання поточної дати
        diff_day = today_date - requested_day #Розрахунок різниці між поточною датою та заданою
        return diff_day.days #Повернення різниці
    except ValueError:
        return "Invalid format. Try entering 'YYYY-MM-DD'" 
print(get_days_from_today('2025-04-04')) #Виклик функції