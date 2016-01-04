from setuptools import setup

requires = [
    'autopep8==1.2.1',
    'pep8==1.6.2',
    'requests==2.8.1',
    'mod-wsgi==4.4.21',
    'mod-wsgi-httpd==2.4.12.6',


    ]

setup(name='AutoShare',
      version='1.0',
      description='An app that automates sharing of video on Facebook wall when uploaded on Youtube',
      author='Trishna Guha',
      author_email='trishnaguha17@gmail.com',
      url='http://autoshare-autoshare.rhcloud.com/',
      install_requires=requires,
     )
