from setuptools import setup

with open('requirements.txt') as f:
    requirements = list(map(lambda x: x.strip(), f.readlines()))

setup(
    name='prosto-sms',
    version='0.0.1',

    author='Alex Dennitsev',
    author_email='me@chydo.dev',

    url="",
    description='ale',

    packages=['prosto_sms'],
    install_requires=requirements,

    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
