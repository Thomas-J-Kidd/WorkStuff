from rich.progress import Progress
import time

class RichProgressBar:
    def __init__(self, total_steps = 100):
        self.total_steps = total_steps
        self.continue_progress = True
        self.progress = Progress()
        self.task = self.progress.add_task("[cyan]Processing...", total=self.total_steps)

    def simulate_process(self):
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing...", total=self.total_steps)
            for i in range(self.total_steps):
                if self.continue_progress:
                # Simulate the process here
                    time.sleep(0.1)
                    progress.update(task, advance=1)
        self.progress.stop()
        

    def end_progress(self):
        self.progress.stop()
        self.progress = None
    

# Example of using the RichProgressBar class
def main():
    total_steps = 100
    progress_bar = RichProgressBar(total_steps)

    try:
        progress_bar.simulate_process()
    except KeyboardInterrupt:
        progress_bar.end_progress()
        print("\nProcess interrupted!")

if __name__ == "__main__":
    main()

