from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import Separator, Token, prompt, style_from_dict

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


questions = [
    {
        "type": "checkbox",
        "message": "Select toppings",
        "name": "toppings",
        "choices": [
            Separator("= The Meats ="),
            {"name": "Ham"},
            {"name": "Ground Meat"},
            {"name": "Bacon"},
            Separator("= The Cheeses ="),
            {"name": "Mozzarella", "checked": True},
            {"name": "Cheddar"},
            {"name": "Parmesan"},
            Separator("= The usual ="),
            {"name": "Mushroom"},
            {"name": "Tomato"},
            {"name": "Pepperoni"},
            Separator("= The extras ="),
            {"name": "Pineapple"},
            {"name": "Olives", "disabled": "out of stock"},
            {"name": "Extra cheese"},
        ],
        "validate": lambda answer: "You must choose at least one topping."
        if len(answer) == 0
        else True,
    }
]

answers = prompt(questions, style=style)
pprint(answers)
