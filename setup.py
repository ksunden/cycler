from setuptools import setup

setup(name='cycler',
      version='0.10.0',
      author='Thomas A Caswell',
      author_email='matplotlib-users@python.org',
      py_modules=['cycler'],
      description='Composable style cycles',
      url='https://github.com/matplotlib/cycler',
      platforms='Cross platform (Linux, Mac OSX, Windows)',
      install_requires=['six'],
      license="BSD",
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      keywords='cycle kwargs',
      )
