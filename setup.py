from setuptools import setup

setup(
    name='plantservice',
    install_requires=[
        'uwsgi',
        'flask',
        'flask-admin',
        'flask-restful',
        'flask-sqlalchemy',
        'psycopg2',
    ],
)
