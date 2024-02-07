import tkinter as tk

# use a boolean variable to help control state of time (running or not running)
running = False

hours, minutes, seconds = 0, 0, 0
time_list = []

def start():
    global running
    start_button.config(state='disabled')
    pause_button.config(state='normal')
    if not running:
        update()
        running = True

def pause():
    global running
    pause_button.config(state='disabled')
    start_button.config(state='normal')
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# reset function
def reset():
    global running
    pause_button.config(state='disabled')
    start_button.config(state='normal')
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00:00')
    # remove flag text
    flag_text.delete("1.0", "end")
    time_list.clear()

# write a time when flag button pressed
def flag():
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    time_list.append(hours_string + ":" + minutes_string + ":" + seconds_string)
    flag_text.delete("1.0", "end")
    flag_text.insert(tk.END, "\n".join(time_list))

# update stopwatch function
def update():
    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)

# create main window
root = tk.Tk()
root.geometry('600x420')
root.title('Stopwatch')

# label to display time
stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 60))
stopwatch_label.pack()

# label to display flag
flag_text = tk.Text(root, height = 7, width = 52)
# flag_text.config(state='disabled')
flag_text.insert(tk.END, "\n".join(time_list))
flag_text.pack()

# start, pause, reset, flag, quit buttons
start_button = tk.Button(text='Start', height=4, width=7, font=('Arial', 20), command=start)
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='Pause', height=4, width=7, font=('Arial', 20), command=pause)
pause_button.config(state='disabled')
pause_button.pack(side=tk.LEFT)
flag_button = tk.Button(text='Flag', height=4, width=7, font=('Arial', 20), command=flag)
flag_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='Reset', height=4, width=7, font=('Arial', 20), command=reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='Quit', height=4, width=7, font=('Arial', 20), command=root.quit)
quit_button.pack(side=tk.LEFT)

root.mainloop()