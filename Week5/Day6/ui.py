from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("KBC")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="abcd", font=('Ariel', 20, 'italic'))

        self.tick_image = PhotoImage(file="images/true.png")
        self.cross_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.tick_image, bg=THEME_COLOR, highlightthickness=0, command=self.answered_true)
        self.true_button.grid(row=3, column=1, padx=10, pady=10)

        self.false_button = Button(image=self.cross_image, bg=THEME_COLOR, highlightthickness=0, command=self.answered_false)
        self.false_button.grid(row=3, column=2, padx=10, pady=10)

        self.score_label = Label(text=f"Score: {self.score}", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Over \n You scored {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answered_true(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def answered_false(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

