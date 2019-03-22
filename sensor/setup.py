from setuptools import setup

def get_reqs():
    with open('requirements.txt', 'r') as fobj:
        reqs = fobj.readlines()
    return [req.strip() for req in reqs]

setup(name='sensor',
      version='1.0',
      description='Robot Weld Sim Sensor Model',
      author='Alejandro Carrillo',
      author_email='alex.emilio.carrillo@gmail.com',
      packages=['sensor'],
      install_requires=get_reqs(),
      entry_points = {
          'console_scripts': ['run-sensor=sensor.__main__']
      }
     )
