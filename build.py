from pybuilder.core import use_plugin, init


use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

#name = "Weather"
version = "1.0"

summary = "Weather PyBuilder / Git project"
url     = "https://github.com/avishekmitra/Weather.git"

authors      = ("Avishek Mitra", "amitraa2012@gamil.com")
license      = "None"
default_task = "publish"

@init
def set_properties(project):
    pass
