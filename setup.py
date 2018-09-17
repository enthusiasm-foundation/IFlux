import os
import os.path
import sys

from setuptools import setup
setup_args = dict (
    name='iflux_kernel',
    version='0.9',
    description= 'A Jupyter kernel for FLUX queries',
    long_description=
'''This module installs a Jupyter kernel for FLUX. It allows sending queries
to an FLUXD runtime and fetching & presenting the results in a notebook.
It is implemented as a Jupyter wrapper kernel, by using the Python 
pyflux library''',
    license='MIT',
    url='https://github.com/enthusiasm-foundation/IFlux',
    download_url = 'https://github.com/enthusiasm-foundation/IFlux',
    author='Enthusiasm Foundation',
    author_email='flux@enthusiasm.foundation',

    packages=[ 'iflux_kernel' ],
    install_requires = [ 'setuptools',
                         'ipykernel >= 4.0',
                         'notebook',
                         'json2html',
                         'traitlets',
                         'matplotlib',
                         'requests',
                         'websocket',
                         'pygments',
                         'pandas', ],
#    extras_require = {
#        'Diagram': [ 'graphviz' ] },

    keywords = ['SPARQL','RDF','Jupyter','kernel'],
    classifiers = [
          'Framework :: IPython',
          'Framework :: Jupyter',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'License :: OSI Approved :: BSD License',
          'Development Status :: 4 - Beta',
          'Topic :: Database :: Front-Ends',
          'Topic :: System :: Shells',
      ],      
  )


if __name__ == '__main__':
    setup( **setup_args )