

import setuptools


setuptools.setup(
    name='clean-arch',
    version='0.0.1',
    description='Clean architecture implementation demo project',
    install_requires=[
        'Inject==4.3.1',
        'attrs',
        'sqlalchemy'
    ],
    python_requires=">=3.8",
    extras_require={
        'dev': [
           'pytest',
           'flake8',
           'mock'
        ]
    },
    entry_points={
        "console_scripts": [
            "auctions = auctions.__main__:main"
        ],
    },
)