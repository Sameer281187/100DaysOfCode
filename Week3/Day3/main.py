from QuestionModel import Question
from Questionnaire import questionnaire
from QuizBrain import QuizBrain

question_bank = []
final_score = 0
for ques in questionnaire:
    question_bank.append(Question(ques["question"], ques["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
