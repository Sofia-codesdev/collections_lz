import numpy as np

def main():
    print("--- Работа с матрицами ---")
    
    # Ввод размерности с проверкой на корректность
    while True:
        try:
            n = int(input("Введите количество строк (N): "))
            m = int(input("Введите количество столбцов (M): "))
            if n > 0 and m > 0:
                break
            else:
                print("Размеры должны быть положительными числами.")
        except ValueError:
            print("Ошибка: введите целые числа.")

    # Создание матрицы случайных чисел (от 1 до 10 для наглядности)
    # np.random.randint(нижняя_граница, верхняя_граница, размер)
    matrix = np.random.randint(1, 10, size=(n, m))
    
    print("\nИсходная матрица:")
    print(matrix)
    
    # Транспонирование матрицы
    transposed_matrix = matrix.T
    
    print("\nТранспонированная матрица:")
    print(transposed_matrix)
    
    # Вычисление определителей
    # Определитель можно вычислить только для квадратных матриц
    if n == m:
        det_original = np.linalg.det(matrix)
        det_transposed = np.linalg.det(transposed_matrix)
        
        print(f"\nОпределитель исходной матрицы: {det_original:.4f}")
        print(f"Определитель транспонированной матрицы: {det_transposed:.4f}")
        
        # Сравнение с учетом погрешности вычислений с плавающей точкой
        if np.isclose(det_original, det_transposed):
            print("Результат: Определители равны (как и должно быть по свойству матриц).")
        else:
            print("Результат: Определители НЕ равны.")
    else:
        print("\nПримечание: Определитель можно вычислить только для квадратной матрицы (N = M).")
        print("Так как матрица прямоугольная, сравнение определителей невозможно.")

if __name__ == "__main__":
    main()