import codecs
import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]

setuptools.setup(
    name="curvature-scale-space",
    version="0.0.2",
    author="Yasser Qureshi",
    author_email="yasser.m.q01@gmail.com",
    description="Curvature Scale-Space for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yasserqureshi1/pycss",
    project_urls={
        "Bug Tracker": "https://github.com/yasserqureshi1/pycss/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['curvature-scale-space'],
    python_requires=">=3.6",
    install_requires=install_reqs
)