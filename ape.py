#!/usr/bin/env python

import subprocess

# ---------------------------------------------------------------------------
# low-level apt and pip

def apt(cmd, package, verbose=False):
    "apt-get install or remove"
    if cmd not in ('install', 'remove'):
        raise ValueError("`cmd` must be 'install' or 'remove'")
    apt_cmd = "apt-get %s -y %s" % (cmd, package)
    if verbose:
        stdout = None
    else:
        stdout = open("/dev/null", "w")
    proc = subprocess.Popen(apt_cmd, shell=True, stdin=None,
                            stdout=stdout, stderr=None,
                            executable="/bin/bash")
    proc.wait()

def pip(cmd, package, verbose=False):
    "pip install or remove"
    if cmd == 'install':
        pip_cmd = "pip install %s" % package
    elif cmd == 'remove':    
        pip_cmd = "pip uninstall -y %s" % package
    else:
        raise ValueError("`cmd` must be 'install' or 'remove'")
    if verbose:
        stdout = None
    else:
        stdout = open("/dev/null", "w")
    proc = subprocess.Popen(pip_cmd, shell=True, stdin=None,
                            stdout=stdout, stderr=None,
                            executable="/bin/bash")
    proc.wait()

# ---------------------------------------------------------------------------
# high-level install and remove functions

def install(pkg_method, verbose=False):
    "install x using apt or pip where pkg_method either 'x.apt' or 'x.pip'"
    install_or_remove('install', pkg_method, verbose)

def remove(pkg_method, verbose=False):
    "remove x using apt or pip where pkg_method either 'x.apt' or 'x.pip'"
    install_or_remove('install', pkg_method, verbose)

def install_or_remove(cmd, pkg_method, verbose=False):
    "install/remove x using apt/pip where pkg_method either 'x.apt' or 'x.pip'"
    pkg, method = pkg_method.split('.')
    if method == 'apt':
        apt(cmd, pkg, verbose)
    elif method == 'pip':
        pip(cmd, pkg, verbose)
    else:
        raise ValueError("`method` must be 'apt' or 'pip'")

# ---------------------------------------------------------------------------
# package list to install

def get_pkg_list():
    pkg_list = [

                # dev tools
                'build-essential.apt',
                'git.apt',
                'gitg.apt',
                'meld.apt',

                # python
                'python-dev.apt',
                'python3.apt',
                'python3-dev.apt',
                'ipython.pip',

                # unit tests
                'nose.pip',
                'virtualenv.pip',
                'tox.pip',
                'python-coverage.apt',

                # misc
                'cython.pip'
                'python-matplotlib.apt',
                'python-sphinx.apt',

                # numpy/scipy
                'gfortran.apt',
                'libblas-dev.apt',
                'libatlas-base-dev.apt',
                'numpy.pip',
                'scipy.pip',

                # h5py
                'libhdf5-serial-dev.apt',
                'h5py.pip',

                ]
    return pkg_list

# ---------------------------------------------------------------------------
# By default install

if __name__ == "__main__":
    verbose = True
    pkg_list = get_pkg_list()
    for pkg_method in pkg_list:
        install(pkg_method, verbose)
