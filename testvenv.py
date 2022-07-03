import pip

_all_ = [
    "yolk=>0.10"
    "SOAPpy>=0.12.22",
    "pycrypto>=2.6.1",
    "suds>=0.4",
    "Python-ldap>=2.4.19",
    "paramiko>=1.15.2",
    "nose>=1.3.4",
    "selenium>=2.44.0",
    "bottle>=0.12.8",
    "CherryPy>=3.6.0",
    "pika>=0.9.14",
]

windows = ["wmi-client-wrapper>=0.0.12",]

linux = ["WMI>=1.4.9",]

darwin = []

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    from sys import platform

    install(_all_) 
    if platform == 'windows':
        install(windows)
    if platform.startswith('linux'):
        install(linux)
    if platform == 'darwin': # MacOS
        install(darwin)