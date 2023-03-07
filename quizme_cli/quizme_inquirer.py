import click
from PyInquirer import prompt, Separator, Token, style_from_dict


style = style_from_dict(
    {
        Token.Separator: "#4169e1",
        Token.QuestionMark: "#673ab7 bold",
        Token.Selected: "#c71585",
        Token.Pointer: "#2e8b57 bold",
        Token.Instruction: "#f0e68c",
        Token.Answer: "#f44336 bold",
        Token.Question: "#808000",
    }
)


# Class Quiz(prompt, question/answers)
class Quiz:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


# Data Questions
tech_questionsList = [
    "Python is a dynamic programming language?",
    "How many kilobytes makes 1 Gigabyte ",
    "These are OOP language except",
    "Which programming language was made in 10 days",
]
tech_questions_optionsList = [
    [{"name": "(a)True"}, {"name": "(b)False"}],
    [
        {
            "name": "(a)100Kb",
        },
        {"name": "(b)1000kb"},
        {"name": "(c)1000000kb"},
    ],
    [
        {
            "name": "(a)Python",
        },
        {"name": "(b)PHP"},
        {"name": "(c)JavaScript"},
        {"name": "(d)Julia"},
        {"name": "(e)Java"},
    ],
    [
        {
            "name": "(a)Python",
        },
        {"name": "(b)JavaScript"},
    ],
]
tech_questions = [
    Quiz(tech_questionsList[0], tech_questions_optionsList[0], "a"),
    Quiz(tech_questionsList[1], tech_questions_optionsList[1], "c"),
    Quiz(tech_questionsList[2], tech_questions_optionsList[2], "d"),
    Quiz(tech_questionsList[3], tech_questions_optionsList[3], "b"),
]


bible_questionsList = [
    "How many books are in the bible?",
    "Who was the oldest man in the bible",
    "The central theme of the bible is?",
    "Jesus had how many disciples",
]

bible_questions_optionsList = [
    [{"name": "(a)66"}, {"name": "(b)39"}, {"name": "(c)70"}],
    [{"name": "(a)Adam"}, {"name": "(b)Methusaleh"}, {"name": "(c)Moses"}],
    [
        {"name": "(a)Jesus as the Savior and King"},
        {"name": "(b)Man is the ultimate"},
        {"name": "(c)The fall of humanity"},
    ],
    [{"name": "(a)12"}, {"name": "(b)70"}],
]

bible_questions = [
    Quiz(bible_questionsList[0], bible_questions_optionsList[0], "a"),
    Quiz(bible_questionsList[1], bible_questions_optionsList[1], "b"),
    Quiz(bible_questionsList[2], bible_questions_optionsList[2], "a"),
    Quiz(bible_questionsList[3], bible_questions_optionsList[3], "a"),
]


def generate_options(questions: Quiz):
    questions_options_style = [
        {
            "type": "checkbox",
            "message": questions.prompt,
            "name": "answer",
            "choices": [],
            "validate": lambda answer: "You must choose at least one answer"
            if len(answer) == 0
            else True,
        }
    ]
    questions_options_style[0]["choices"].append(Separator("= Choose your answer ="))
    for opt in questions.options:
        questions_options_style[0]["choices"].append(opt)
    questions_options_style[0]["choices"].append(Separator("======================"))
    return questions_options_style


# Fxn
def run_quiz(questions):
    score = 0
    for question in questions:
        user_input = prompt(generate_options(question), style=style)
        answer = user_input["answer"][0][1:2]
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
