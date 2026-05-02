# import tkinter as tk
# from threading import Thread
# from voice import speak, listen, set_ui_callback
# from commands import execute

# #

# def log_user(text):
#     chat_box.insert(tk.END, "You: " + text + "\n")
#     chat_box.see(tk.END)

# def log_jarvis(text):
#     chat_box.insert(tk.END, "Jarvis: " + text + "\n")
#     chat_box.see(tk.END)

# def ui_output(text):
#     log_jarvis(text)

# set_ui_callback(ui_output)

#  #

# def send_command():
#     cmd = entry.get()
#     print("Clicked Send:", cmd)

#     if not cmd.strip():
#         return

#     entry.delete(0, tk.END)
#     log_user(cmd)

#     result = execute(cmd.lower())

#     if result == False:
#         root.quit()

# def start_voice():
#     Thread(target=voice_loop).start()

# def voice_loop():
#     while True:
#         command = listen()

#         if not command:
#             continue

#         log_user(command)
#         result = execute(command)

#         if result == False:
#             break



# root = tk.Tk()
# root.title("Jarvis AI Assistant")
# root.geometry("600x600")

# title = tk.Label(root, text="JARVIS AI", font=("Arial", 20, "bold"))
# title.pack(pady=10)

# chat_box = tk.Text(root, height=20, width=70)
# chat_box.pack(pady=10)

# entry = tk.Entry(root, width=50)
# entry.pack(pady=5)

# BUTTONS (FIXED)
# send_btn = tk.Button(root, text="Send", command=send_command)
# send_btn.pack(pady=5)

# voice_btn = tk.Button(root, text="Sta rt Voice", command=start_voice)
# voice_btn.pack(pady=5)

# exit_btn = tk.Button(root, text="Exit", command=root.quit)
# exit_btn.pack(pady=5)

# root.mainloop()