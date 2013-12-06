from setuptools import setup, find_packages

version = '4.3.0.3'

setup(name='tomcom.plone.csssort',
      version=version,
      description='',
      long_description=open("README.md").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Intended Audience :: Other Audience",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        ],
      keywords='',
      author='tomcom GmbH',
      author_email='kai.hoppert@tomcom.de',
      url='https://pypi.python.org/pypi/tomcom.plone.csssort',
      license='GPL version 2',
      packages=find_packages(),
      namespace_packages=['tomcom','tomcom.plone'],
      include_package_data=True,
      install_requires=[
        'setuptools',
        'tomcom.plone.base',
      ],
      extras_require={'test': [
        'collective.testcaselayer',
      ]},
      platforms='Any',
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = plone
''',
)