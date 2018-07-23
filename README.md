# Xcut
Xcut is an Enhanced cut command, which is used to help grep column.

[![](https://img.shields.io/pypi/pyversions/xcut.svg?longCache=True)](https://pypi.org/pypi/xcut/)
[![](https://img.shields.io/pypi/v/xcut.svg?maxAge=36000)](https://pypi.org/pypi/xcut/)

## Install

    pip install xcut
    pip3 install xcut

## Usage
Cut fields

    > ~ xcut -f job,name test/test.csv
    job,name
    coder,Jack
    artist,Lucy

### set title type
The default title type is head: 

    > ~ xcut -f name,gender -tt head test/test.csv

Set title type as index:

    > ~ xcut -f 1,3 -tt index  test/test.csv
    1,3
    name,job
    Jack,coder
    Lucy,artist

Set title type as custom( you could pass custom titles via `--titles`)

    > ~ xcut -f '职业,姓名' --titles '姓名,性别,职业' test/test.csv -od $'\t'
    职业 姓名
    job	name
    coder	Jack
    artist	Lucy

### set input delimiter(d)

    > ~ xcut -f job,name test/test.csv -d ',' -od '`'
    job`name
    coder`Jack
    artist`Lucy

### Set output delimiter(od)

    > ~ xcut -f job,name test/test.csv -od '`' 
    job`name
    coder`Jack
    artist`Lucy

### output pretty
You could set the output delimiter(od), also you can print it via `pretty`

    > ~ xcut -f '职业,姓名' --titles '姓名,性别,职业' test/test.csv -od $'\t' --tab 20 --pretty
    职业                  姓名
    ----------------------------------------
    job                 name
    coder               Jack
    artist              Lucy


## Required
1. python>=3.5
