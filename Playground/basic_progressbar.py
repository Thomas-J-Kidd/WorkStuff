import sys
import time

def progress_bar(percentage):
    bar_length = 50
    block = int(round(bar_length * percentage))
    progress = f"\r[{'=' * block}{' ' * (bar_length - block)}] {percentage * 100:.2f}%"
    sys.stdout.write(progress)
    sys.stdout.flush()

# Simulate a process that takes some time
def simulate_process():
    for i in range(101):
        progress_bar(i / 100)
        time.sleep(0.1)

simulate_process()
print("\nProcess completed!")
