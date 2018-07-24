# Xcut
Xcut is an Enhanced cut command, which is used to help grep column.

[![](https://img.shields.io/pypi/pyversions/xcut.svg?longCache=True)](https://pypi.org/pypi/xcut/)
[![](https://img.shields.io/pypi/v/xcut.svg?maxAge=36000)](https://pypi.org/pypi/xcut/)
![](https://travis-ci.org/ahuigo/xcut.svg?branch=master)

## Install

    pip install xcut
    pip3 install xcut

## Usage
Let's test a file named `test.csv`

    > ~ cat test/test.csv
    name,gender,job
    Jack,male,coder
    Lucy,female,artist

Cut fields

    > ~ xcut -f job,name test/test.csv
    job,name
    coder,Jack
    artist,Lucy

### Set title type
The default title type is head: `-t head` 

    > ~ xcut -f name,gender test/test.csv

Set title type to index: `-t index`

    > ~ xcut -f 1,3 -t index  test/test.csv
    1,3
    name,job
    Jack,coder
    Lucy,artist

Set title type to custom(`--titles TITLES`)

    > ~ xcut -f '职业,姓名' --titles '姓名,性别,职业' test/test.csv -od $'\t'
    职业 姓名
    job	name
    coder	Jack
    artist	Lucy

Set title type to kv(`-t kv`)

    > ~ echo 'key1=v1,key2=v2,key3=v3' | xcut -f key3,key2 -t kv
    key3,key2
    v3,v2

### Set input delimiter(d)

    > ~ xcut -f job,name test/test.csv -d ',' -od '`'
    job`name
    coder`Jack
    artist`Lucy

### Set output delimiter(od)

    > ~ xcut -f job,name test/test.csv -od '`' 
    job`name
    coder`Jack
    artist`Lucy

### pretty output 
You could set the output delimiter(od), also you can print it via `pretty`

    > ~ xcut -f '职业,姓名' --titles '姓名,性别,职业' test/test.csv -od $'\t' --tab 20 --pretty
    职业                  姓名
    ----------------------------------------
    job                 name
    coder               Jack
    artist              Lucy

## Required
1. python>=3.5
