from setuptools import setup

setup(
    name='pastes_api',
    packages=['pastes_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'mysqlclient',
        'requests',
        'flask-script',
        'redis'
    ]
)
