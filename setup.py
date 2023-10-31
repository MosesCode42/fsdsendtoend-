from setuptools import find_packages, setup 

setup(
    name='DiamondPricePrediction',
    version='0.0.1.dev0',
    author='moses omondi',
    author_email='moseaiml@gmail.com',
     install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)