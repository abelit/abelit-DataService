# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2020/03/21 08:31:18
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from setuptools import setup

setup(
    name='Flask-DataService',
    version='1.0',
    url='http://www.dataforum.com/dataservice/',
    project_urls={
        "Documentation": "https://dataforum.org/dataservice/document",
        "Code": "https://github.com/abelit/abelit-dataservice",
        "Issue tracker": "https://github.comabelit/abelit-dataservice/issues"
    },
    license='BSD',
    author='Abelit',
    author_email='ychenid@live.com',
    maintainer="Abelit",
    maintainer_email="ychenid@live.com",
    description='A Data Science and Role,Permission API.',
    long_description=__doc__,
    python_requires="3.*",
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        "PyMySQL",
        "flask-restful",
        "uwsgi",
        "Flask-SQLAlchemy",
        "Flask-Migrate",
        "Flask-Script",
        "Flask-JWT-Extended",
        "Flask-Cors",
        "itsdangerous"
    ],
    classifiers=[
        'Data Science :: Data Analysis :: Data Visualization',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
