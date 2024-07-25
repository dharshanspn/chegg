import subprocess

commands = [
    'cd probable-chainsaw',
    'pip install google-colab-selenium',
    'pip install google-colab-selenium[undetected]',
]

for command in commands:
    subprocess.call(command, shell=True, stderr=subprocess.DEVNULL)
