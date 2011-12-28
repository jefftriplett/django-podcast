from setuptools import setup, find_packages

template_patterns = [
    'templates/*.html',
    'templates/*/*.html',
]

packages = find_packages('.')

setup(
    name='django-podcast',
    version='0.1dev',
    description='Django podcast app',
    packages=packages,
    package_data=dict((package_name, template_patterns) for package_name in packages),
    classifiers = ['Frameword :: Django'],
)
