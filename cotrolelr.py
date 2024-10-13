from pynput import keyboard
import vgamepad as vg

# Initialize the virtual Xbox gamepad
gamepad = vg.VX360Gamepad()

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char == 'e':
            print("Key 'e' pressed. Simulating left stick button.")
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
    except AttributeError:
        pass

def on_release(key):
    try:
        if hasattr(key, 'char') and key.char == 'e':
            print("Key 'e' released. Stopping left stick button simulation.")
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
    except AttributeError:
        pass
    if key == keyboard.Key.esc:
        return False

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Script stopped by user.")
