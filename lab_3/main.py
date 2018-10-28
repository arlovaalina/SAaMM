from random import *
from tkinter import *
from variables import *
from stateMatrix import *

def get_requests_in_queue(requests_in_queue, curr_state, pi2):
    if (curr_state == 2 or curr_state == 3 or curr_state == 4 or
    curr_state == 5 or curr_state == 6 or curr_state == 7 or
    curr_state == 8) and (pi2 == 0):
        return requests_in_queue + 1
    return requests_in_queue

def get_absolute_throughput(a, curr_state, pi2):
    if (curr_state == 2 or curr_state == 3 or curr_state == 4 or
    curr_state == 5 or curr_state == 6 or curr_state == 7 or
    curr_state == 8) and (pi2 == 0):
        return a + 1
    return a

def get_queue_length(gueue_length, curr_state):
    if curr_state == 4 or curr_state == 5:
        return gueue_length + 1
    if curr_state == 6 or curr_state == 7 or curr_state == 8:
        return gueue_length + 2
    return gueue_length

def get_new_state(graph, curr_state, state):
    for i in range(STATE_AMOUNT):
        transition = graph[curr_state][i]
        if state in transition:
            return i


def start_algorithm(p, pi1, pi2, tacts_amount):
    graph = get_state_matrix()
    gueue_length = 0
    a = 0
    requests_in_queue = 0
    
    
    curr_state = 0
    for tact in range(tacts_amount):
        random_p = 1 if random() <= p else 0
        random_pi1 = 1 if random() <= pi1 else 0
        random_pi2 = 1 if random() <= pi2  else 0
        state = (random_p << 2) + (random_pi1 << 1) + random_pi2
        
        gueue_length = get_queue_length(gueue_length, curr_state)
        a = get_absolute_throughput(a, curr_state, random_pi2)
        requests_in_queue = get_requests_in_queue(requests_in_queue, curr_state, random_pi2)
        
        new_state = get_new_state(graph, curr_state, state)
        curr_state = new_state
    average_gueue_length = gueue_length / tacts_amount
    absolute_throughput = a / tacts_amount
    
    print('time', gueue_length / requests_in_queue)
    print('formula', average_gueue_length / absolute_throughput)
    print('average_gueue_length', average_gueue_length)
    print('absolute_throughput', absolute_throughput)
    

    # aperiodic_interval_label = Label(root, text = "Длина отрезка апериодичности: " + str(round(aperiodic_interval, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 500)
    # indirect_indications_label = Label(root, text = "2К / N: " + str(round(indirect_indications, 3)) + "; pi / 4: " + str(round(math.pi / 4, 3)), height = 1, width = 50, anchor = 'w').place(x = 200, y = 520)
    

def initialize_window():
    root = Tk()
    root.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

    p_label = Label(root, text = "Вероятность не выдачи заявки, ρ").place(x = 10, y = 10)
    p_input = Entry(root, width = 27)
    p_input.place(x = 10, y = 30)
    
    pi1_label = Label(root, text = "Вероятность просеивания, π1").place(x = 10, y = 60)
    pi1_input = Entry(root, width = 27)
    pi1_input.place(x = 10, y = 80)
    
    pi2_label = Label(root, text = "Вероятность просеивания, π2").place(x = 10, y = 110)
    pi2_input = Entry(root, width = 27)
    pi2_input.place(x = 10, y = 130)
    
    tacts_label = Label(root, text = "Количество тактов").place(x = 10, y = 160)
    tacts_input = Entry(root, width = 27)
    tacts_input.place(x = 10, y = 180)
    
    start_button = Button(root, text = "Моделировать", width = 15,
        command = lambda: start_algorithm(float(p_input.get()), float(pi1_input.get()), float(pi2_input.get()), int(tacts_input.get())))
    start_button.place(x = 10, y = 210)

    root.mainloop()


def main():
    initialize_window();

if __name__ == "__main__":
    main()
