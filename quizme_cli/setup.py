from setuptools import setup

setup(
    name="cli-tools",
    version="1.0",
    py_modules=["quizme", "quizme_inquirer"],
    install_requires=["Click", "requests"],
    entry_points={
        "console_scripts": ["quizme=quizme:main", "quizme_inq=quizme_inquirer:main"]
    },  # greetingsコマンド=greeterモジュールのgreetメソッド
)
