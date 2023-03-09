from setuptools import setup

setup(
    name="cli-tools",
    version="1.0",
    py_modules=[""],
    install_requires=["Click", "requests"],
    entry_points={
        "console_scripts": ["covid=covid:main", "covid_cli=covid_cli:main"]
    },  # greetingsコマンド=greeterモジュールのgreetメソッド
)
