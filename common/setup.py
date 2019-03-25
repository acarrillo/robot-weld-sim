from setuptools import setup

def get_reqs():
    with open('requirements.txt', 'r') as fobj:
        reqs = fobj.readlines()
    return [req.strip() for req in reqs]

setup(name='common',
      version='1.0',
      description='Robot Weld Sim Common Library',
      author='Alejandro Carrillo',
      author_email='alex.emilio.carrillo@gmail.com',
      packages=['common'],
      install_requires=get_reqs()
     )
