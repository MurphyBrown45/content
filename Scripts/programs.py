import pyautogui
import time
import tkinter as tk


def poop(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')
        time.sleep(1)

    for _ in range(count):
        pyautogui.write("osascript -e \"set volume output volume 100\"")
        pyautogui.press('enter')
        pyautogui.write("afplay Audio/Fart.mp3")
        pyautogui.press('enter')
        time.sleep(0.5)


def hernia(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')
        time.sleep(3)

    for _ in range(count):
        pyautogui.write("cmd /c start images/hernia.jpg")
        pyautogui.press('enter')


def alert(count):
    for _ in range(count):
        pyautogui.write("osascript -e 'display alert \"virus detected\" message \"your computer has virus\"'")
        pyautogui.press('enter')
        time.sleep(1)

    pyautogui.write("osascript -e 'display alert \"too many virus\" message \"shutting down\"'")
    pyautogui.press('enter')
    pyautogui.write("sudo shutdown -h now")
    pyautogui.press('enter')


def allofit(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')

    for _ in range(count):
        pyautogui.write("start images/gabbs.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/gerny.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/realistic_angry_bird.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/angry_bird_3.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/brods.jpg")
        pyautogui.press('enter')


def crash(count):
    for _ in range(1):
        pyautogui.write("osascript -e 'display alert \"Your computer has a virus\" message \"shutting down \"'")
        pyautogui.press('enter')

        pyautogui.write("sudo shutdown -h now")
        pyautogui.press('enter')


def dysentery(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')

    for _ in range(count):
        pyautogui.write("osascript -e \"set volume output volume 100\"")
        pyautogui.press('enter')

        pyautogui.write("afplay Audio/Fart.mp3")
        pyautogui.press('enter')

        pyautogui.write("afplay Audio/beanfrong.mp3")
        pyautogui.press('enter')
        time.sleep(0.5)


def shelly(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')

    for _ in range(count):
        pyautogui.write("start images/Shelly.jpg")
        pyautogui.press('enter')


def poopwin(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')
        time.sleep(2)

    for _ in range(count):
        pyautogui.write("start Audio/Fart.mp3")
        pyautogui.press('enter')
        time.sleep(7)


def sutwin(count):
    for _ in range(1):
        pyautogui.write("cmd /c shutdown -s -t 0")
        pyautogui.press('enter')


def bswin(count):
    for _ in range(1):
        pyautogui.write("cd content")
        pyautogui.press('enter')

    for _ in range(count):
        pyautogui.write("start images/gerny.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/gabbs.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/hernia.jpg")
        pyautogui.press('enter')

        pyautogui.write("start images/angry_bird.png")
        pyautogui.press('enter')

        pyautogui.write("start images/curiouskirk.jpg")
        pyautogui.press('enter')

    for _ in range(count):
        pyautogui.write("start Audio/Fart.mp3")
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write("start Audio/beanfrong.mp3")
        pyautogui.press('enter')
        time.sleep(1)


def get_count():
    try:
        value = int(count_var.get())
        if value < 1:
            value = 1
    except ValueError:
        value = 1
    count_var.set(str(value))
    current_count_label.config(text=f"Current count: {value}")
    return value


def update_count_label(*args):
    try:
        current = int(count_var.get())
        if current < 1:
            current = 1
    except ValueError:
        current = 1
    current_count_label.config(text=f"Current count: {current}")


root = tk.Tk()
root.title('Program Control Panel')

count_var = tk.StringVar(value='1')

count_frame = tk.Frame(root)
count_frame.pack(padx=10, pady=(10, 0), fill='x')

count_label = tk.Label(count_frame, text='Count:')
count_label.pack(side='left')

count_entry = tk.Entry(count_frame, textvariable=count_var, width=5)
count_entry.pack(side='left', padx=(5, 0))

current_count_label = tk.Label(count_frame, text='Current count: 1')
current_count_label.pack(side='left', padx=(15, 0))

count_var.trace_add('write', update_count_label)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

buttons = [
    ('poop', lambda: poop(get_count())),
    ('hernia', lambda: hernia(get_count())),
    ('alert', lambda: alert(get_count())),
    ('allofit', lambda: allofit(get_count())),
    ('crash', lambda: crash(get_count())),
    ('dysentery', lambda: dysentery(get_count())),
    ('shelly', lambda: shelly(get_count())),
    ('poopwin', lambda: poopwin(get_count())),
    ('sutwin', lambda: sutwin(get_count())),
    ('bswin', lambda: bswin(get_count())),
]

for text, action in buttons:
    btn = tk.Button(button_frame, text=text, width=20, command=action)
    btn.pack(pady=2)

root.mainloop()
