from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiztastic")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", bg=THEME_COLOR, fg="white", height=3, width=6,
                                font=("Arial", 12, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=35)

        self.true_button = Button(borderwidth=0, highlightthickness=0, pady=20, command=self.true_pressed)
        true_image = PhotoImage(file="images/true.png")
        self.true_button.config(image=true_image)
        self.true_button.grid(column=0, row=2, )

        self.false_button = Button(borderwidth=0, highlightthickness=0, pady=20, command=self.false_pressed)
        false_image = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_image)
        self.false_button.grid(column=1, row=2)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Thank you for playing!\n"
                                                            f"Your final score was {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)

