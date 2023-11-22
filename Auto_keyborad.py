import time
import keyboard
import mouse
import subprocess

class KeyboardMouseController:
    def __init__(self ,json_reader):
        self.json_reader =json_reader
        pass
    def run (self):
        loaded_actions = self.json_reader.get_value("actions")
        if loaded_actions is not None:
            # Execute the loaded actions
            self.execute_actions(loaded_actions)


    def _validate_key(self, key):
        # Add any key validation logic here
        return key  # Placeholder; customize as needed

    def _validate_button(self, button):
        # Add any mouse button validation logic here
        return button  # Placeholder; customize as needed

    def _validate_action(self, action):
        # Add any action validation logic here
        return action  # Placeholder; customize as needed

    def _simulate_key_press(self, key, modifiers=None, duration=0.1):
        key = self._validate_key(key)
        modifiers = [self._validate_key(mod) for mod in modifiers] if modifiers else []

        # Press the modifiers
        for mod in modifiers:
            keyboard.press(mod)

        # Press and release the key
        keyboard.press(key)
        time.sleep(duration)
        keyboard.release(key)

        # Release the modifiers
        for mod in modifiers:
            keyboard.release(mod)

        time.sleep(0.1)  # Additional sleep for stability


    def _simulate_mouse_click(self, button, duration=0.1):
        button = self._validate_button(button)
        mouse.click(button)
        time.sleep(duration)

    def _simulate_text_typing(self, text, interval=0.1):
        for char in text:
            keyboard.write(char)
            time.sleep(interval)

    def _simulate_run_command(self, command, duration=1):
        subprocess.Popen(command, shell=True)
        time.sleep(duration)

    def execute_actions(self, actions):
        for action in actions:
            action_type = action.get("type")
            if action_type == "key":
                self._simulate_key_press(action.get("key"), action.get("modifiers"), action.get("duration", 0.1))
            elif action_type == "button":
                self._simulate_mouse_click(action.get("button"), action.get("duration", 0.1))
            elif action_type == "text":
                self._simulate_text_typing(action.get("text", ""), action.get("interval", 0.1))
            elif action_type == "run":
                self._simulate_run_command(action.get("command"), action.get("duration", 1))
            else:
                print(f"Unknown action type: {action_type}")


