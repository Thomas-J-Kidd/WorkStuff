from tqdm import tqdm
import time

def simulate_process():
    total_steps = 100
    for i in tqdm(range(total_steps), desc="Processing...", ncols=100):
        # Simulate the process here
        time.sleep(0.1)

simulate_process()
print("\nProcess completed!")

