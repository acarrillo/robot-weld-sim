from setuptools import setup

def get_reqs():
    with open('requirements.txt', 'r') as fobj:
        reqs = fobj.readlines()
    return [req.strip() for req in reqs]

setup(name='viewer',
      version='1.0',
      description='Robot Weld Sim Viewer',
      author='Alejandro Carrillo',
      author_email='alex.emilio.carrillo@gmail.com',
      packages=['viewer'],
      install_requires=get_reqs()
     )
