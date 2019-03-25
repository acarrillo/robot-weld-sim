from setuptools import setup

def get_reqs():
    with open('requirements.txt', 'r') as fobj:
        reqs = fobj.readlines()
    return [req.strip() for req in reqs]

setup(name='controller',
      version='1.0',
      description='Robot Weld Sim Controller Model',
      author='Alejandro Carrillo',
      author_email='alex.emilio.carrillo@gmail.com',
      packages=['controller'],
      install_requires=get_reqs(),
      entry_points = {
          'console_scripts': ['run-controller=controller.__main__:main']
      }
     )
