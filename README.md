# CONTENTS OF THIS FILE

- Introduction
- Installation
- Run


## INTRODUCTION

- Save multiple web pages as PDF with Background Graphics using selenium webdriver.


## INSTALLATION

### Install webdriver

```shell
$ sudo apt install chromium-chromedriver
```

### Create a Virtual environment

- I install all my virtual environments in ~/.envs directory


> create virual environment named saveaspdfenv and activate it

```shell
$ mkdir ~/.envs && cd ~/.envs 

$ python3 -m venv saveaspdfenv

$ source saveaspdfenv/bin/activate

```

### Clone

- Clone this repo to your local machine using `https://github.com/fvcproductions/SOMEREPO`

> Navigate into Documents directory and clone this repo
```shell
$ $ cd ~/Documents
$ git clone https://github.com/JenishRudani98/SaveAsPdf.git
$ cd SaveAsPdf
```
> install required modules 

```shell
$ python3 -m pip install -r requirements.txt
```



## Run

To use this application go into tests directory and run main.py, You can make changes into main.py according to your preference.

```shell
  $ cd tests

  $ python3 main.py
```
