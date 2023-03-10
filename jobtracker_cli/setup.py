from setuptools import setup

setup(
    name="cli-tools",
    version="1.0",
    py_modules=[""],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "jobtracker=jobtracker:main",
            "jobtracker_cli=jobtracker_cli:main"
        ]
    },  # greetingsコマンド=greeterモジュール:greetメソッド
)
