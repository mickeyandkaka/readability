#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from py_read import py_read

if __name__ == '__main__':
    obj = py_read("http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/");

    print(obj.title)
    print(obj.content)