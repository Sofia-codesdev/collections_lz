import pandas as pd
import os

# Имя файла для сохранения данных
FILENAME = "address_book.csv"

# Определяем столбцы для DataFrame
COLUMNS = ["ФИО", "Адрес", "Телефон", "Дата рождения"]

def load_data():
    """Загружает данные из файла, если он существует, иначе создает пустой DataFrame."""
    if os.path.exists(FILENAME):
        return pd.read_csv(FILENAME)
    return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    """Сохраняет DataFrame в файл."""
    df.to_csv(FILENAME, index=False)
    print("Данные успешно сохранены в файл.")

def display_data(df):
    """Выводит текущую адресную книгу."""
    if df.empty:
        print("\nАдресная книга пуста.")
    else:
        print("\nТекущая адресная книга:")
        print(df.to_string(index=False))

def add_entry(df):
    """Добавляет новую запись."""
    print("\n--- Добавление новой записи ---")
    fio = input("Введите ФИО: ")
    address = input("Введите Адрес: ")
    phone = input("Введите Телефон: ")
    dob = input("Введите Дату рождения (ДД.ММ.ГГГГ): ")
    
    # Создаем новую строку и добавляем ее в DataFrame
    new_row = pd.DataFrame([[fio, address, phone, dob]], columns=COLUMNS)
    df = pd.concat([df, new_row], ignore_index=True)
    print("Запись добавлена.")
    return df

def delete_entry(df):
    """Удаляет запись по ФИО."""
    print("\n--- Удаление записи ---")
    fio = input("Введите ФИО записи, которую хотите удалить: ")
    
    # Ищем индексы строк, где ФИО совпадает
    indices = df[df['ФИО'] == fio].index
    if len(indices) > 0:
        df = df.drop(indices).reset_index(drop=True)
        print("Запись удалена.")
    else:
        print("Запись с таким ФИО не найдена.")
    return df

def edit_entry(df):
    """Изменяет запись по ФИО."""
    print("\n--- Изменение записи ---")
    fio = input("Введите ФИО записи, которую хотите изменить: ")
    
    indices = df[df['ФИО'] == fio].index
    if len(indices) > 0:
        idx = indices[0] # Берем первую найденную запись
        print(f"Текущие данные: {df.loc[idx].to_dict()}")
        
        field = input("Какое поле изменить? (ФИО/Адрес/Телефон/Дата рождения): ")
        if field in COLUMNS:
            new_value = input(f"Введите новое значение для '{field}': ")
            df.at[idx, field] = new_value
            print("Запись обновлена.")
        else:
            print("Ошибка: Неверное название поля.")
    else:
        print("Запись с таким ФИО не найдена.")
    return df

def main():
    """Главная функция с интерфейсом меню."""
    df = load_data()
    
    while True:
        print("\n" + "="*30)
        print("МЕНЮ АДРЕСНОЙ КНИГИ:")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Удалить запись")
        print("4. Изменить запись")
        print("5. Сохранить и выйти")
        print("="*30)
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            display_data(df)
        elif choice == '2':
            df = add_entry(df)
        elif choice == '3':
            df = delete_entry(df)
        elif choice == '4':
            df = edit_entry(df)
        elif choice == '5':
            save_data(df)
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.")

if __name__ == "__main__":
    main()