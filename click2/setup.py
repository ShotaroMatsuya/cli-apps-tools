from setuptools import setup

setup(
    name="cli-tools",
    version="1.0",
    py_modules=[""],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "basic=basic_cli:main",
            "args=args_cli:main",
            "var=var_cli:main",
            "group=group_cli:main",
            "sub_group=sub_group_cli:main",
            "ctx=ctx_cli:main",
            "prompt=prompt_cli:main",
            "confirm=confirm_cli:download",
            "color=colors_cli:main",
            "launch=launch_cli:main",
            "show_help=show_help_cli:main",
        ]
    },  # greetingsコマンド=greeterモジュールのgreetメソッド
)
