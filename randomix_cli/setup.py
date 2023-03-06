from setuptools import setup

setup(
    name="cli-tools",
    version="1.0",
    py_modules=[""],
    install_requires=["Click", "requests"],
    entry_points={
        "console_scripts": [
            "randomix=randomix_click:main",
        ]
    },  # greetingsコマンド=greeterモジュールのgreetメソッド
)