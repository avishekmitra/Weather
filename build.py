from pybuilder.core import use_plugin, init

##use_plugin("exec")
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")



name='Weather'
version="1.0"
author='Avishek Mitra'

summary="Weather PyBuilder / Git project"
url="https://github.com/avishekmitra/Weather.git"

default_task="publish"


@init
def set_properties(project):
    project.set_property("coverage_break_build", False) #deafult is true
    project.build_depends_on("mockito")

