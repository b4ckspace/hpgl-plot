from setuptools import setup

setup(
    name='plotter',
    packages=['sendhpgl'],
    include_package_data=True,
    install_requires=[
        'pyserial',
    ],
    entry_points={
        'console_scripts': [
            'sendhpgl=sendhpgl.__main__:main'
        ]
    }
)
