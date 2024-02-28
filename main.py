import random
import time
from tkinter import *
from tkinter import messagebox

def jacobi_symbol(a, n):
    if n % 2 == 0:
        raise ValueError("Jacobi symbol is defined only for odd n")
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        if n % 8 == 1 or n % 8 == 7:
            return 1
        if n % 8 == 3 or n % 8 == 5:
            return -1
    if a >= n:
        return jacobi_symbol(a % n, n)
    if a % 2 == 0:
        return jacobi_symbol(2, n) * jacobi_symbol(a // 2, n)  # Multiplicative property
    if a % 4 == 3 and n % 4 == 3:
        return -jacobi_symbol(n, a)  # Quadratic reciprocity
    return 1  # Default to 1 if the Jacobi symbol is not explicitly calculated

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def power(a, d, n):
        result = 1
        a %= n
        while d > 0:
            if d % 2 == 1:
                result = (result * a) % n
            d //= 2
            a = (a * a) % n
        return result

    def test_ss(a, n):
        if power(a, (n - 1) // 2, n) == 1:
            jacobi = jacobi_symbol(a, n)
            if jacobi is None:
                return False
            if jacobi == -1:
                jacobi = n - 1
            return jacobi % n == power(a, (n - 1) // 2, n) % n
        return False

    iterations = 0
    for _ in range(k):
        a = random.randint(2, n - 1)
        if not test_ss(a, n):
            return False, iterations
        iterations += 1
    return True, iterations

def generate_prime_number(bits):
    start_time = time.time()
    iterations = 0
    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1  # Set the most significant and least significant bits to 1
        is_prime_result, prime_iterations = is_prime(n)
        iterations += prime_iterations
        if is_prime_result:
            end_time = time.time()
            time_taken = end_time - start_time
            return n, time_taken, iterations

# Чтение входных данных из файла
"""with open('input.txt', 'r') as file:
    input_data = file.readlines()
    bits = int(input_data[0].strip())
    probability = int(input_data[1].strip())

prime_number, generation_time, total_iterations = generate_prime_number(bits)
print(f"Сгенерированное простое число: {prime_number}")
print(f"Время генерации: {generation_time} секунд")
print(f"Количество итераций: {total_iterations}")
"""

#-----------------------------------------------------------------------------------------------#
def insert_data_from_file():
    try:
        with open('input.txt', 'r') as file:
            input_data = file.readlines()
            height_tf.insert(0, input_data[0].strip())
            weight_tf.insert(0, input_data[1].strip())
    except FileNotFoundError:
        messagebox.showerror('Error', 'File not found')

def calculate_main():
    bits = int(height_tf.get())
    probability = int(weight_tf.get())
    # Далее можно использовать переменные bits и iterations для вычислений
    prime_number, generation_time, total_iterations = generate_prime_number(bits)
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.truncate(0)
        f.write(f'Сгенерированное простое число: {prime_number}\n Время генерации: {generation_time}\n Количество итераций: {total_iterations}')
    messagebox.showinfo('hello', f'Сгенерированное простое число: {prime_number}\n Время генерации: {generation_time}\n Количество итераций: {total_iterations}')

window = Tk()
window.title('Генератор чисел')
window.geometry('500x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="Введите колличество bits"
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Введите вероятность генерации простого числа",
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Сгенерировать число',
    command=calculate_main
)
cal_btn.grid(row=5, column=2)

cal_btn = Button(
    frame,
    text='Вставить данные из файла',
    command=insert_data_from_file
)
cal_btn.grid(row=5, column=1)

window.mainloop()
