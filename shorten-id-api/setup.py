from setuptools import setup

setup(
    name='shorten_id_api',
    packages=['shorten_id_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv'
    ]
)
