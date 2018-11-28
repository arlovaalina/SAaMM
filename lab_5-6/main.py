from random import *
from tkinter import *
from variables import *
import math
import numpy

def generate_numbers(a, r, m, numbersAmount):
    numbers = []
    for i in range(numbersAmount):
        rNew = (a * r) % m
        x = rNew / m
        r = rNew
        numbers.append(x)
    return numbers

def generate_process_time(amount, mean, standard_deviation):
    N = 6
    numbers = generate_numbers(A_VALUE, R_VALUE, M_VALYE, amount * N)
    result = []
    for i in range(0, len(numbers), N):
        sub_numbers = numbers[i:i + N]
        x = mean + standard_deviation * math.sqrt(12 / N) * (sum(sub_numbers) - N / 2)
        result.append(x)
    return result
    
def get_free_channel(channels):
    for i, channel in enumerate(channels):
        if (channel == 0):
            return i
    return None

def start_algorithm(root, mean, standard_deviation, minutes_amount):
    channels = [0, 0, 0]
    process_time = [round(x) for x in generate_process_time(minutes_amount, mean * 60, standard_deviation * 60)]
    requests_amount = 0
    rejected_requests = 0
    processed_requests = 0
    total_busy_channels_amount = 0
    
    times = numpy.random.poisson(0.033, minutes_amount)

    for current_minute in range(minutes_amount):
        if (times[current_minute] == 1):            
            free_channel_index = get_free_channel(channels)
            if free_channel_index is None:
                rejected_requests += 1
            else:
                channels[free_channel_index] = process_time[current_minute]
                processed_requests += 1
            requests_amount += 1
        
        total_busy_channels_amount += len(list(filter(lambda x: x != 0, channels)))
        channels = list(map(lambda x: x - 1 if x != 0 else 0, channels))
    
    
    print(requests_amount)
    print(rejected_requests)
    p_reject = rejected_requests / requests_amount
    busy_channels_amount = total_busy_channels_amount / minutes_amount
    absolute_throughput = processed_requests / minutes_amount * 60
            
    p_reject_label = Label(root, text = "Вероятность отказа: " + str(round(p_reject, 4)), height = 1, width = 50, anchor = 'w').place(x = 300, y = 10)
    busy_channels_amount_label = Label(root, text = "Среднее число занятых каналов: " + str(round(busy_channels_amount, 4)), height = 1, width = 50, anchor = 'w').place(x = 300, y = 50)
    absolute_throughput_label = Label(root, text = "Абсолютная пропускная способность: " + str(round(absolute_throughput, 4)), height = 1, width = 50, anchor = 'w').place(x = 300, y = 90)

def initialize_window():
    root = Tk()
    root.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    
    m_label = Label(root, text = "Математическое ожидание, m").place(x = 10, y = 10)
    m_input = Entry(root, width = 30)
    m_input.place(x = 10, y = 30)
    
    sigma_label = Label(root, text = "Среднеквадратическое отклонение, σ").place(x = 10, y = 60)
    sigma_input = Entry(root, width = 30)
    sigma_input.place(x = 10, y = 80)
    
    amount_label = Label(root, text = "Количество минут, N").place(x = 10, y = 110)
    amount_input = Entry(root, width = 30)
    amount_input.place(x = 10, y = 130)
    
    start_button = Button(root, text = "Моделировать", width = 20,
        command = lambda: start_algorithm(root, float(m_input.get()), float(sigma_input.get()), int(amount_input.get())))
    start_button.place(x = 10, y = 160)

    root.mainloop()


def main():
    initialize_window();

if __name__ == "__main__":
    main()
