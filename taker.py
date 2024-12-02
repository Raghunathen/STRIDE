import os
import time
from datetime import datetime
import mss
from threading import Thread
from queue import Queue
from pynput import keyboard

# Directory to store unsorted screenshots by action
base_dir = "ProperDataset"
actions = ['left', 'right', 'up', 'down', 'noop']

# Queue to handle background saving of screenshots
save_queue = Queue()

# Counter for each action to ensure unique filenames
action_counter = {action: 0 for action in actions}

# Variable to hold the current action
current_action = 'noop'

# Function to create directories if they don't exist
def create_dirs():
    for action in actions:
        dir_path = os.path.join(base_dir, action)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# Function to save screenshots in the background
def save_screenshot_worker():
    while True:
        file_path, screenshot = save_queue.get()
        if file_path is None:
            break  # Stop the thread if None is passed
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=file_path)
        print(f"Screenshot saved: {file_path}")
        save_queue.task_done()

# Function to handle key press events
def on_press(key):
    global current_action
    try:
        if key == keyboard.Key.left:
            current_action = 'left'
        elif key == keyboard.Key.right:
            current_action = 'right'
        elif key == keyboard.Key.up:
            current_action = 'up'
        elif key == keyboard.Key.down:
            current_action = 'down'
    except AttributeError:
        pass

# Function to handle key release events
def on_release(key):
    global current_action
    if key in [keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.down]:
        current_action = 'noop'
    if key == keyboard.Key.esc:
        # Stop listener on ESC key
        return False

# Main function to take screenshots of a specific region and save them based on keypresses
def main():
    create_dirs()
    
    # Define the bounding box for the specific region
    monitor = {
        "left": 350,   # x-coordinate for the top-left corner
        "top": 180,    # y-coordinate for the top-left corner
        "width": 740,  # width of the capture region
        "height": 690  # height of the capture region
    }

    # Start the background saving thread
    save_thread = Thread(target=save_screenshot_worker, daemon=True)
    save_thread.start()

    # Start the keyboard listener in a separate thread
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    with mss.mss() as sct:
        try:
            while True:
                # Use the global `current_action` for the current action
                action = current_action

                # Grab the screenshot of the defined region
                screenshot = sct.grab(monitor)
                
                # Update the action counter and generate a unique filename
                action_counter[action] += 1
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
                file_path = os.path.join(base_dir, action, f"{action}_{action_counter[action]}_{timestamp}.png")

                # Queue the screenshot for saving in the respective action folder
                save_queue.put((file_path, screenshot))

                # Adjust delay as necessary to avoid excessive CPU usage
                time.sleep(0.05)

        except KeyboardInterrupt:
            pass  # Allow graceful exit with Ctrl+C
        finally:
            # Stop the save thread and wait for all screenshots to be saved
            save_queue.put((None, None))
            save_queue.join()
            listener.stop()

if __name__ == "__main__":
    main()
import os
import time
from datetime import datetime
import mss
from threading import Thread
from queue import Queue
from pynput import keyboard

# Directory to store unsorted screenshots by action
base_dir = "new_shots"
actions = ['left', 'right', 'up', 'down', 'noop']

# Queue to handle background saving of screenshots
save_queue = Queue()

# Counter for each action to ensure unique filenames
action_counter = {action: 0 for action in actions}

# Variables to track current action and noop count
current_action = 'noop'
noop_count = 0

# Function to create directories if they don't exist
def create_dirs():
    for action in actions:
        dir_path = os.path.join(base_dir, action)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# Function to save screenshots in the background
def save_screenshot_worker():
    while True:
        file_path, screenshot = save_queue.get()
        if file_path is None:
            break  # Stop the thread if None is passed
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=file_path)
        print(f"Screenshot saved: {file_path}")
        save_queue.task_done()

# Function to handle key press events
def on_press(key):
    global current_action, noop_count
    try:
        if key == keyboard.Key.left:
            current_action = 'left'
        elif key == keyboard.Key.right:
            current_action = 'right'
        elif key == keyboard.Key.up:
            current_action = 'up'
        elif key == keyboard.Key.down:
            current_action = 'down'
        else:
            current_action = 'noop'
            noop_count = 0  # Reset noop count when a non-noop action occurs
    except AttributeError:
        pass

# Function to handle key release events
def on_release(key):
    global current_action
    if key in [keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.down]:
        current_action = 'noop'
    if key == keyboard.Key.esc:
        # Stop listener on ESC key
        return False

# Main function to take screenshots of a specific region and save them based on keypresses
def main():
    create_dirs()
    
    # Define the bounding box for the specific region
    monitor = {
        "left": 300,   # x-coordinate for the top-left corner
        "top": 170,    # y-coordinate for the top-left corner
        "width": 740,  # width of the capture region
        "height": 690  # height of the capture region
    }

    # Start the background saving thread
    save_thread = Thread(target=save_screenshot_worker, daemon=True)
    save_thread.start()

    # Start the keyboard listener in a separate thread
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    with mss.mss() as sct:
        global noop_count
        try:
            while True:
                # Use the global `current_action` for the current action
                action = current_action

                # Increment noop count if the action is noop
                if action == 'noop':
                    noop_count += 1
                else:
                    noop_count = 0  # Reset the noop count for non-noop actions

                # Save a screenshot only if it's a non-noop action
                # or every 5 consecutive noops
                if action != 'noop' or (noop_count == 100):
                    if noop_count == 100:
                        noop_count = 0  # Reset noop count after saving

                    # Grab the screenshot of the defined region
                    screenshot = sct.grab(monitor)

                    # Update the action counter and generate a unique filename
                    action_counter[action] += 1
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
                    file_path = os.path.join(base_dir, action, f"{action}_{action_counter[action]}_{timestamp}.png")

                    # Queue the screenshot for saving in the respective action folder
                    save_queue.put((file_path, screenshot))


        except KeyboardInterrupt:
            pass  # Allow graceful exit with Ctrl+C
        finally:
            # Stop the save thread and wait for all screenshots to be saved
            save_queue.put((None, None))
            save_queue.join()
            listener.stop()

if __name__ == "__main__":
    main()
