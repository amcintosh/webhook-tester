import io

from setuptools import find_packages, setup

setup(
    name='webhook-tester',
    version='1.0.0',
    url='https://www.freshbooks.com/api/webhooks',
    license='BSD',
    maintainer='FreshBooks',
    maintainer_email='dev@freshbooks.com',
    description='Test FB Webhooks with this endpoint.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    '''extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },'''
)