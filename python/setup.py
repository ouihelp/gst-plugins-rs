from setuptools import setup

try:
    from setuptools.command.bdist_wheel import bdist_wheel
except ImportError:  # pragma: no cover
    from wheel.bdist_wheel import bdist_wheel


class PlatformWheel(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        _python, _abi, platform = super().get_tag()
        return ("py3", "none", platform)


setup(cmdclass={"bdist_wheel": PlatformWheel})
