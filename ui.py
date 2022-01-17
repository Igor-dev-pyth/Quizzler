from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Courier", 10)

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Access to quiz_brain object
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="aaa", font=QUESTION_FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, bd=0, activebackground=THEME_COLOR,
                                   command=self.right)
        self.check_button.grid(column=0, row=2)
        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, bd=0, activebackground=THEME_COLOR,
                                   command=self.wrong)
        self.cross_button.grid(column=1, row=2)
        self.score_label = Label(text="Score: ", bg=THEME_COLOR, fg="white", font=SCORE_FONT)
        self.score_label.grid(column=1, row=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="#b3ffb3")
        else:
            self.canvas.config(bg="#ffad99")
        self.window.after(1000, self.get_next_question)
