#!/usr/bin/env python

# Copyright (c) 2013, Berkeley Analytics, LLC.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import subprocess

# ---------------------------------------------------------------------------
# default package list

def get_pkg_list():
    "Default package list; for apt-get uses ubuntu package names"
    pkg_list = [

                # pip
                'python-pip.apt',

                # dev tools
                'build-essential.apt',
                'git.apt',
                'gitg.apt',
                'meld.apt',
                'grin.pip',
                'flake8.pip',
                'exuberant-ctags.apt',

                # python
                'python-dev.apt',
                'python3.apt',
                'python3-dev.apt',
                'ipython.pip',
                'ipdb.pip',

                # unit tests
                'nose.pip',
                'virtualenv.pip',
                'tox.pip',
                'python-coverage.apt',

                # numpy/scipy
                'gfortran.apt',
                'libblas-dev.apt',
                'libatlas-base-dev.apt',
                'numpy.pip',
                'scipy.pip',

                # matplotlib
                'libfreetype6-dev.apt',
                'libpng-dev.apt',
                'matplotlib.pip',

                # misc
                'cython.pip',
                'python-sphinx.apt',

                # h5py
                'libhdf5-serial-dev.apt',
                'h5py.pip',

                # non-development
                'texlive-extra-utils.apt',
                'latex-beamer.apt',
                'gnucash.apt',
                'revelation.apt',
                'vim-gnome.apt',
                'gnome-search-tool.apt',
                'workrave.apt',

                ]
    return pkg_list

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
# low-level install and remove functions

def apt(cmd, package, verbose=False):
    "apt-get install or remove"
    if cmd not in ('install', 'remove'):
        raise ValueError("`cmd` must be 'install' or 'remove'")
    apt_cmd = "apt-get %s -y %s" % (cmd, package)
    shell_call(apt_cmd, verbose)

def pip(cmd, package, verbose=False):
    "pip install or remove"
    if cmd == 'install':
        pip_cmd = "pip install %s" % package
    elif cmd == 'remove':
        pip_cmd = "pip uninstall -y %s" % package
    else:
        raise ValueError("`cmd` must be 'install' or 'remove'")
    shell_call(pip_cmd, verbose)

def shell_call(cmd, verbose):
    if verbose:
        stdout = None
        n = len(cmd)
        print('=' * n)
        print(cmd)
        print('=' * n)
    else:
        stdout = open("/dev/null", "w")
    proc = subprocess.Popen(cmd, shell=True, stdout=stdout,
                            executable="/bin/bash")
    proc.wait()

# ---------------------------------------------------------------------------
# By default install

if __name__ == "__main__":
    verbose = True
    pkg_list = get_pkg_list()
    for pkg_method in pkg_list:
        install(pkg_method, verbose)
