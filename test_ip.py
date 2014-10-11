# -*- coding: utf-8 -*-

import sys
PY3 = sys.version_info[0] == 3

if PY3:
    def u(s):
        return s
else:
    def u(s):
        return s.decode('utf-8')


import IP


def test_ip():
    assert IP.find("127.0.0.1") == u("本机地址\t本机地址")
    assert IP.find("59.151.24.1") == u("中国\t北京\t北京")


def test_domain():
    assert IP.find("localhost") == u("本机地址\t本机地址")
    assert IP.find("ele.me") == u("中国\t北京\t北京")


def test_without_mmap():
    with IP.IPv4Database(use_mmap=False) as db:
        assert db.find("127.0.0.1") == u("本机地址\t本机地址")
