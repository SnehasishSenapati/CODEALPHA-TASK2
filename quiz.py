class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):
        score = 0
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")
            
            user_answer = int(input("Enter the number of your answer: ")) - 1

            if user_answer == question.correct_option:
                print("Correct!\n")
                score += 1
            else:
                print("Wrong!\n")

        print(f"You got {score} out of {len(self.questions)} questions correct.")


# Example Usage
if __name__ == "__main__":
    quiz = Quiz("Math Quiz")

    q1 = Question("What is 2 + 2?", ["3", "4", "5"], 1)
    q2 = Question("What is 5 * 6?", ["20", "25", "30"], 2)
    q3 = Question("What is 8 / 2?", ["2", "4", "8"], 1)

    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)

    print(f"Welcome to the {quiz.name}!")
    quiz.start_quiz()
