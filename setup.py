from setuptools import setup


setup(
    name='cldfbench_visserkalamang',
    py_modules=['cldfbench_visserkalamang'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'visserkalamang=cldfbench_visserkalamang:Dataset',
        ]
    },
    install_requires=[
        'cldfbench[excel]>=1.3.0',
        'pylexibank>=2.8.2',
        'idspy>=0.2',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
