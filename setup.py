from setuptools import setup, find_packages
from os.path import join, dirname
# read the contents of your README file

setup(
    name='hmtai',
    version='3.2.2',
    license='CC-BY-NC-ND-4.0',
    author="NickSaltFoxu",
    author_email='thnyawec@gmail.com',
    packages=['hmtai'],
    url='https://discord.gg/vJs36ES',
    keywords= ["anime", "hentai", "nsfw", "sfw", "images", "gifs", "wallpaper", "discord", "ahegao", "ass", "neko", "yuri", "panties", "thighs", "ero", "kawaii", "cute", "waifu", "hmtai", "zettaiRyouiki", "18+", "REST", "API", "Mikun"],
    long_description=open('README.md', encoding='UTF8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
          'requests',
      ],
)
