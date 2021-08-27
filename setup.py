import os

from setuptools import find_packages, setup


PACKAGE_DIRNAME = 'adjust_time'
ROOT_DIR = os.path.dirname(__file__)

with open(os.path.join(ROOT_DIR, 'README.md')) as readme:
    README = readme.read()


def get_version() -> str:
    """packageのバージョンを取得します
    実体は `PACKAGE_DIRNAME / version.py` に記載しておいてそれを取得するしくみ
    """
    version_filepath = os.path.join(ROOT_DIR, 'src', PACKAGE_DIRNAME, 'version.py')
    with open(version_filepath) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split()[-1][1:-1]
    assert False

def _lines_from_file(filename):
    with open(os.path.join(ROOT_DIR, filename)) as f:
        lines = f.readlines()
    return lines

def get_extra_requires():
    extras = {
        # テスト用のパッケージ
        'test': ['pytest'],
        # ドキュメント生成用パッケージ
        'document': ['sphinx', 'sphinx_rtd_theme']
    }
    return extras


setup(
    name='adjust_time',
    version=get_version(),
    author='sinchir0',
    packages=find_packages("src"),
    package_dir={"":"src"},
    include_package_data=True,
    license='BSD License',
    description='',
    long_description=README,
    long_description_content_type='text/markdown',
    url='',
    author_email='',
    install_requires=_lines_from_file('requirements.txt'),
    extras_require=get_extra_requires(),
)
