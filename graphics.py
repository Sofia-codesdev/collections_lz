import matplotlib.pyplot as plt
import numpy as np

def main():
    # Создаем массив значений X от 0.1 до 5 чтобы избежать log(0) и отрицательных значений для ln
    x = np.linspace(0.1, 5, 500)
    
    # Вычисляем значения функций
    y1 = x**2
    y2 = np.exp(x)
    y3 = np.log(x)
    y4 = x**3
    
    # Создаем фигуру и оси
    plt.figure(figsize=(10, 6))
    
    # Строим графики линиями разных цветов
    plt.plot(x, y1, label='x^2', color='blue')
    plt.plot(x, y2, label='e^x', color='red')
    plt.plot(x, y3, label='ln(x)', color='green')
    plt.plot(x, y4, label='x^3', color='purple')
    
    # Выделяем точки для целых значений X
    # Берем целые числа от 1 до 5, так как 0 нельзя брать для ln(x)
    int_x = np.arange(1, 6)
    
    # Отмечаем точки на каждой функции разными маркерами
    plt.plot(int_x, int_x**2, 'o', color='blue', markersize=8)         # точки (круги)
    plt.plot(int_x, np.exp(int_x), 'x', color='red', markersize=8)     # кресты
    plt.plot(int_x, np.log(int_x), 's', color='green', markersize=8)   # квадраты
    plt.plot(int_x, int_x**3, '^', color='purple', markersize=8)       # треугольники
    
    # Настройка графика
    plt.title("Графики функций: x^2, e^x, ln(x), x^3")
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    
    # Ограничиваем ось Y, чтобы график e^x не сжимал остальные функции
    plt.ylim(-5, 30) 
    
    plt.grid(True) # Добавляем сетку для удобства
    plt.legend()   # Показываем легенду
    
    # Отображаем график
    plt.show()

if __name__ == "__main__":
    main()