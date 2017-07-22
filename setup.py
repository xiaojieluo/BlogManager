from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = ['dove', 'dove.tools']
test_requirements = ['pytest>=3.1.2']
entry_points = {
    'console_scripts': [
        'dove-quickstart = dove.tools.dove_quickstart:main'
    ]
}

setup(
    name='dove',
    keywords='static vlog, management',
    version='0.0.1',
    description='A static blog with background management',
    long_description=readme,
    author='Luo Xiaojie',
    author_email='xiaojieluoff@gmail.com',
    url='https://github.com/xiaojieluo/dove',
    license=license,
    packages=packages,
    tests_require=test_requirements,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    test_suite='tests',
    python_requires='>=3',
    entry_points=entry_points,
)
