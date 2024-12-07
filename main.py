import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

def show_question():
    question = quiz_data[current_question]
    question_number = current_question + 1 
    qs_label.config(text="Question {}: {}".format(question_number, question["question"]))
    
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")
    
    feedback_label.config(text="")
    next_btn.config(state="disabled")
    progress_bar['value'] = (current_question + 1) / len(quiz_data) * 100  

def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")
    
    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score : {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="✔ Correct!", foreground="green")
    else:
        feedback_label.config(text="✘ Incorrect!", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal") 

def next_question():
    global current_question
    current_question += 1
    
    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", 
                            "Quiz Completed! Final score : {}/{}".format(score, len(quiz_data)))
        root.destroy()


root = tk.Tk()
root.title("Quiz App")
root.geometry("700x600")  
root.configure(bg="#f0f8ff")

style = Style(theme="flatly")
style.configure("TLabel", font=("Arial", 14, "bold"), background="#f0f8ff")  
style.configure("TButton", font=("Arial", 12), padding=5, width=25, relief="flat", background="#4CAF50")  
style.configure("TFrame", background="#f0f8ff")  


qs_label = ttk.Label(root, anchor="center", wraplength=600, padding=(20,))
qs_label.pack(pady=(20, 10))  


choices_frame = ttk.Frame(root, style="TFrame")
choices_frame.pack(pady=(20, 10)) 


choice_btns = []
for i in range(4):
    button = ttk.Button(choices_frame, command=lambda i=i: check_answer(i))
    button.grid(row=i//2, column=i%2, padx=10, pady=10, ipadx=5, ipady=5)
    choice_btns.append(button)


feedback_label = ttk.Label(root, anchor="center", padding=10, font=("Arial", 12))
feedback_label.pack(pady=(10, 20))

score = 0
score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_data)), anchor="center", font=("Arial", 14), padding=10)
score_label.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=600, mode="determinate")
progress_bar.pack(pady=(20, 10))

next_btn = ttk.Button(root, text="Next", command=next_question, state="disabled")
next_btn.pack(pady=10)


current_question = 0
show_question()

root.mainloop()
