import click
from PyInquirer import prompt


# Class Quiz(prompt, question/answers)
class Quiz:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# Data Questions
tech_questionsList = [
    "Python is a dynamic programming language?\n(a)True,\n(b)False\n\n",
    "How many kilobytes makes 1 Gigabyte \n(a)100Kb,\n(b)1000kb\n(c)1000000kb\n\n",
    "These are OOP language except\n(a)Python,\n(b)PHP,\n(c)JavaScript,\n(d)Julia,\n(b)Java\n\n",
    "Which programming language was made in 10 days\n(a)Python,\n(b)JavaScript,\n\n",
]
tech_questions = [
    Quiz(tech_questionsList[0], "a"),
    Quiz(tech_questionsList[1], "c"),
    Quiz(tech_questionsList[2], "d"),
    Quiz(tech_questionsList[3], "b"),
]

bible_questionsList = [
    "How many books are in the bible?\n(a)66,\n(b)39,\n(b)70\n\n",
    "Who was the oldest man in the bible\n(a)Adam,\n(b)Methusaleh\n(c)Moses\n\n",
    "The central theme of the bible is?\n(a)Jesus as the Savior and King,\n(b)Man is the ultimate,\n(c)The fall of humanity\n\n",
    "Jesus had how many disciples\n(a)12,\n(b)70,\n\n",
]

bible_questions = [
    Quiz(bible_questionsList[0], "a"),
    Quiz(bible_questionsList[1], "b"),
    Quiz(bible_questionsList[2], "a"),
    Quiz(bible_questionsList[3], "a"),
]


# Fxn
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        print(answer)
        if answer == question.answer:
            score += 1
    click.secho(
        "You scored {} out of {}".format(score, len(questions)), fg="white", bg="blue"
    )


@click.group()
@click.version_option(prog_name="quizme", version="0.01")
def main():
    """Quizme CLI"""
    pass


# quizme start
@main.command()
def start():
    """Start Quiz"""
    click.echo("Starting Quiz")
    quiz_type = [
        {
            "type": "list",
            "name": "questiontype",
            "message": "Question Type",
            "choices": ["Tech", "Bible", "History", "Sports"],
        }
    ]
    ans_quiz_type = prompt(quiz_type)

    if ans_quiz_type["questiontype"] == "Tech":
        click.echo("Starting")
        run_quiz(tech_questions)

    elif ans_quiz_type["questiontype"] == "Bible":
        click.echo("Starting")
        run_quiz(bible_questions)

    elif ans_quiz_type["questiontype"] == "History":
        click.echo("Starting")
        run_quiz()


# quizme info
@main.command()
def info():
    """Info about Quizme CLI"""
    click.echo("QuizMe CLI")
