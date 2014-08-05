17MonIP Python Lib
==================

.. image:: http://img.shields.io/pypi/v/17MonIP.svg?style=flat
   :target: https://pypi.python.org/pypi/17MonIP

.. image:: http://img.shields.io/travis/lxyu/17monip/master.svg?style=flat
   :target: https://travis-ci.org/lxyu/17monip

.. image:: http://img.shields.io/pypi/dm/17MonIP.svg?style=flat
   :target: https://pypi.python.org/pypi/17MonIP

IP search based on 17mon.cn, the best IP database for china.

Source: http://tool.17mon.cn


Install
-------

.. code:: bash

    $ pip install 17monip

Usage
-----

.. code:: python

    >>> import IP
    >>> IP.find("www.baidu.com")
    '中国\t浙江\t杭州'
    >>> IP.find("127.0.0.1")
    '本机地址\t本机地址'


CMD Util
--------

.. code:: bash

    $ iploc ele.me
    中国    北京    北京
    $ iploc aliyun.com
    中国    浙江    杭州


Changelog
---------

https://github.com/lxyu/17monip/blob/master/CHANGES.rst
