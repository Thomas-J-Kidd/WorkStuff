from halo import Halo
import time

def simulate_process():
    with Halo(text="Processing...", spinner="dots"):
        total_steps = 100
        for _ in range(total_steps):
            # Simulate the process here
            time.sleep(0.1)

simulate_process()
print("\nProcess completed!")

