import tkinter as tk
import keyboard

ks = "space"
kp = "up"

def check_keypress(event):
    global key1, key2

    # Check if key1 is pressed
    if key1.get() and event.name == key1.get() and event.event_type == "down":
        print("Key 1 is pressed!")
        keyboard.press(ks)  # Simulate pressing the 'a' key

    # Check if key2 is pressed
    if key2.get() and event.name == key2.get() and event.event_type == "down":
        print("Key 2 is pressed!")
        keyboard.press(kp)  # Simulate pressing the 'b' key

    # Check if key1 or key2 are released
    if (event.name == key1.get() or event.name == key2.get()) and event.event_type == "up":
        keyboard.release(ks)  # Release the 'a' key
        keyboard.release(kp)  # Release the 'b' key

root = tk.Tk()
root.title("Key Press Detection")

# Create and position the first label and input box
label1 = tk.Label(root, text="Key 1:")
label1.grid(row=0, column=0)
key1 = tk.Entry(root)
key1.grid(row=0, column=1)

# Create and position the second label and input box
label2 = tk.Label(root, text="Key 2:")
label2.grid(row=1, column=0)
key2 = tk.Entry(root)
key2.grid(row=1, column=1)

output_text = tk.Text(root, height=10, width=40)
output_text.grid(row=2, columnspan=2, padx=10, pady=10)

# Redirect print statements to the Text widget
def redirect_print(output_text):
    def print_to_text(*args, **kwargs):
        output_text.insert(tk.END, " ".join(map(str, args)) + "\n")
    return print_to_text

print_to_text = redirect_print(output_text)
print = print_to_text


# Start the keypress detection using keyboard.hook()
keyboard.hook(check_keypress)

root.mainloop()
