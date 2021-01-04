from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='vmx_editor',
    packages=['vmx_editor'],
    version='0.3.2',
    license='MIT',
    description='Read and edit .vmx configurations file programmatically',
    long_description=long_description,
    author='lennisthemenace',
    author_email='no@email.com',
    url='https://github.com/lennisthemenace/vmx_editor',
    download_url='https://github.com/lennisthemenace/vmx_editor/archive/0.3.2.tar.gz',
    keywords=['VMX', 'EDITOR', 'VMWARE'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
