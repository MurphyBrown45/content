
import time
import tkinter as tk
import os
import shutil
import subprocess
from tkinter import ttk


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#paths to gitbash
def _find_git_bash():
    bash_path = shutil.which("bash")
    if bash_path:
        return bash_path

    candidates = [
        r"C:\Program Files\Git\bin\bash.exe",
        r"C:\Program Files (x86)\Git\bin\bash.exe",
        r"C:\Program Files\Git\usr\bin\bash.exe",
        r"C:\Program Files (x86)\Git\usr\bin\bash.exe",
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    return None

GIT_BASH = _find_git_bash()
_bash_process = None


def _ensure_bash():
    global _bash_process
    if _bash_process and _bash_process.poll() is None:
        return _bash_process
    if not GIT_BASH:
        return None

    creationflags = subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
    _bash_process = subprocess.Popen(
        [GIT_BASH, "--login", "-i"],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
        creationflags=creationflags,
    )
    time.sleep(0.5)
    return _bash_process


def _run(command):
    if not command:
        return 0

    if GIT_BASH:
        proc = _ensure_bash()
        if proc and proc.stdin:
            proc.stdin.write(command + "\n")
            proc.stdin.flush()
            return 0

    return os.system(command)


def _cd_content():
    if GIT_BASH:
        _run("cd content")
    else:
        os.chdir(os.path.join(BASE_DIR, "content"))


def _open(path):
    if GIT_BASH:
        _run(f'cmd.exe /C start "" "{path}"')
    else:
        os.system(f'start "" "{path}"')


def _play_audio(path):
    _open(path)


def poop(count):
    for _ in range(1):
        _run("")
        time.sleep(1)

    for _ in range(count):
        _run('echo "set volume output volume 100"')
        _play_audio("Audio/Fart.mp3")
        time.sleep(0.5)


def hernia(count):
    for _ in range(1):
        _cd_content()
        time.sleep(3)

    for _ in range(count):
        _open("images/hernia.jpg")


def alert(count):
    for _ in range(count):
        _run('cmd.exe /C msg * "virus detected: your computer has virus"')
        time.sleep(1)


def allofit(count):
    for _ in range(1):
        _cd_content()

    for _ in range(count):
        _open("images/gabbs.jpg")
        _open("images/gerny.jpg")
        _open("images/realistic_angry_bird.jpg")
        _open("images/angry_bird_3.jpg")
        _open("images/brods.jpg")


def crash(count):
    for _ in range(1):
        _run('cmd.exe /C msg * "Your computer has a virus: shutting down"')

        _run('cmd.exe /C shutdown -s -t 0')


def dysentery(count):
    for _ in range(1):
        _cd_content()

    for _ in range(count):
        _run('echo "set volume output volume 100"')
        _play_audio("Audio/Fart.mp3")
        _play_audio("Audio/beanfrong.mp3")
        time.sleep(0.5)


def shelly(count):
    for _ in range(1):
        _cd_content()

    for _ in range(count):
        _open("images/Shelly.jpg")


def poopwin(count):
    for _ in range(1):
        _cd_content()
        time.sleep(2)

    for _ in range(count):
        _open("Audio/Fart.mp3")
        time.sleep(7)


def shutwin(count):
    countdown_seconds = 20
    shutdown_window = tk.Toplevel(root)
    shutdown_window.title("Shutdown Countdown")
    shutdown_window.geometry("320x100")
    shutdown_window.resizable(False, False)
    shutdown_window.transient(root)

    timer_label = tk.Label(shutdown_window, text=f"Shutting down in {countdown_seconds} seconds...", font=("Arial", 14))
    timer_label.pack(expand=True, padx=10, pady=15)

    def update_timer():
        nonlocal countdown_seconds
        if countdown_seconds <= 0:
            timer_label.config(text="Shutting down now...")
            return
        timer_label.config(text=f"Shutting down in {countdown_seconds} seconds...")
        countdown_seconds -= 1
        root.after(1000, update_timer)

    _run("cmd /c shutdown -s -t 20")
    update_timer()


def bswin(count):
    for _ in range(1):
        _cd_content()

    for _ in range(count):
        _open("images/gerny.jpg")
        _open("images/gabbs.jpg")
        _open("images/hernia.jpg")
        _open("images/angry_bird.png")
        _open("images/curiouskirk.jpg")
        _open("images/Shelly.jpg")

    for _ in range(count):
        _open("Audio/Fart.mp3")
        time.sleep(7)
        _open("Audio/beanfrong.mp3")
        time.sleep(3)


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
root.title('PCP')
style = ttk.Style()
style.theme_use("clam")

style.configure("Poop.TButton", background = "blue", font = ("Arial", 12))  
style.configure("Hernia.TButton", background = "green", font = ("Arial", 12))
style.configure("Alert.TButton", background = "blue", font = ("Arial", 12))
style.configure("AllOfIt.TButton", background = "green", font = ("Arial", 12))
style.configure("Crash.TButton", background = "green", font = ("Arial", 12))
style.configure("Dysentery.TButton", background = "blue", font = ("Arial", 12))
style.configure("Shelly.TButton", background = "green", font = ("Arial", 12))
style.configure("PoopWin.TButton", background = "green", font = ("Arial", 12))
style.configure("ShutWin.TButton", background = "red", font = ("Arial", 12))
style.configure("BSWin.TButton", background = "green", font = ("Arial", 12))

count_var = tk.StringVar(value='1')

count_frame = tk.Frame(root)
count_frame.pack(padx=10, pady=(10, 0), fill='x')

count_label = tk.Label(count_frame, text='Count:')
count_label.pack(side='left')

count_entry = tk.Entry(count_frame, textvariable=count_var, width=5)
count_entry.pack(side='left', padx=(5, 0))

current_count_label = tk.Label(count_frame)
current_count_label.pack(side='left', padx=(15, 0))

count_var.trace_add('write', update_count_label)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

buttons = [
    ('poop', lambda: poop(get_count()), 'Poop.TButton'),
    ('hernia', lambda: hernia(get_count()), 'Hernia.TButton'),
    ('alert', lambda: alert(get_count()), 'Alert.TButton'),
    ('allofit', lambda: allofit(get_count()), 'AllOfIt.TButton'),
    ('crash', lambda: crash(get_count()), 'Crash.TButton'),
    ('dysentery', lambda: dysentery(get_count()), 'Dysentery.TButton'),
    ('shelly', lambda: shelly(get_count()), 'Shelly.TButton'),
    ('poopwin', lambda: poopwin(get_count()), 'PoopWin.TButton'),
    ('shutwin', lambda: shutwin(get_count()), 'ShutWin.TButton'),
    ('bswin', lambda: bswin(get_count()), 'BSWin.TButton'),
]

for text, action, style_name in buttons:
    btn = ttk.Button(button_frame, text=text, width=20, command=action, style=style_name)
    btn.pack(pady=2)

root.mainloop()
