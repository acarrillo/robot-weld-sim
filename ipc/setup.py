from setuptools import setup

def get_reqs():
    with open('requirements.txt', 'r') as fobj:
        reqs = fobj.readlines()
    return [req.strip() for req in reqs]

setup(name='ipc',
      version='1.0',
      description='Robot Weld Sim IPC Library',
      author='Alejandro Carrillo',
      author_email='alex.emilio.carrillo@gmail.com',
      packages=['ipc'],
      install_requires=get_reqs()
     )
