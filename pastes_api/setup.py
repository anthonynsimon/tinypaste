from setuptools import setup

setup(
    name='pastes_api',
    packages=['pastes_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'schema',
        'flask-mysqldb'
    ]
)
