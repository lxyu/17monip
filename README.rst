17MonIP Python Lib
==================

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

    $ ip ele.me
    中国    北京
    $ ip aliyun.com
    中国    浙江    杭州
