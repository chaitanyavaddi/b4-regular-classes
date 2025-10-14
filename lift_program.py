import os
import time

floors = 6
requests = [3, 5, 1, 3]
current_floor = 0

def draw_lift(current):
    current = 5 - current
    print('🏢 LIFT SIMULATION')
    for floor in range(floors):
        if floor == current: #3, 3
            print(f"   🟫 | 🚇 |") #lift body
        else:
            print(f"   🟦 |    |") #floor wihtout lift


#MAIN LOGIC
print('Starting lift simulation..\n')


for request in requests:
    print(f'Moving to floor: {request}')
    time.sleep(2)
    draw_lift(request)


            




