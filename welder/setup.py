from setuptools import setup

def get_reqs():
    with open('requirements.txt', 'r') as fobj:
        reqs = fobj.readlines()
    return [req.strip() for req in reqs]

setup(name='welder',
      version='1.0',
      description='Robot Weld Sim Welder Model',
      author='Alejandro Carrillo',
      author_email='alex.emilio.carrillo@gmail.com',
      packages=['welder'],
      install_requires=get_reqs()
     )
