from setuptools import setup

setup(
    name='gloop-lib',
    packages=['gloop', 'gloop.channels'],
    install_requires=[
        'aiohttp==3.7.4',
         'aioredis==1.3.0',
         'async-timeout==3.0.1',
         'atomicwrites==1.3.0',
         'attrs==19.3.0',
         'certifi==2019.9.11',
         'chardet==3.0.4',
         'docker==4.1.0',
         'hiredis==1.0.0',
         'idna==2.8',
         'importlib-metadata==0.23',
         'more-itertools==7.2.0',
         'multidict==4.5.2',
         'packaging==19.2',
         'pluggy==0.13.0',
         'py==1.8.0',
         'pyparsing==2.4.4',
         'pytest==5.2.2',
         'pytest-mock==1.11.2',
         'requests==2.22.0',
         'six==1.13.0',
         'urllib3==1.25.6',
         'wcwidth==0.1.7',
         'websocket-client==0.56.0',
         'yarl==1.3.0',
         'zipp==0.6.0'
    ],
    url='https://github.com/pitzer42/gloop-lib',
    license='MIT',
    author='Arthur Pitzer',
)
