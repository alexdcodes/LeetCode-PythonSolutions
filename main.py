import subprocess, locale
import paramiko
procObj = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1])
print(outputStr)

alex = dict(name='alex', job='dev', age='30')
print(alex)


def print_hi(name):
    print(f'Just a sandbox, {name}')


if __name__ == '__main__':
    print_hi('env')

