#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'Weather',
        version = '1.0',
        description = 'Weather PyBuilder / Git project',
        long_description = '',
        author = '',
        author_email = '',
        license = '',
        url = 'https://github.com/avishekmitra/Weather.git',
        scripts = ['scripts/weather-pybuilder.py'],
        packages = [],
        namespace_packages = [],
        py_modules = [
            '__init__',
            'core',
            'helpers',
            'loghelpers',
            'subhelpers'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
