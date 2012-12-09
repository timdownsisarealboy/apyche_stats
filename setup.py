from setuptools import setup, find_packages

setup(
    name='apyche_stats',
    version='1.0',
    description='Simple API for Apache Stats',
    author='Tim Downs',
    author_email='timothy.j.downs@gmail.com',
    zip_safe=False,
    include_package_data=True,
    url='http://www.tjdownsllc.com/',
    platforms=["any"],
    install_requires=[
        'Django==1.3',
	'django-piston',
	'gunicorn'
    ]
)
