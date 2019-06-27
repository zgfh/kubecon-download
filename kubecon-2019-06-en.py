#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 2019/6/26 5:49 PM
"""

import kubecon

if __name__ == '__main__':
    kubecon.Main('events', [
        "https://kccncosschn19eng.sched.com/2019-06-{}/overview?iframe=no&w=100%&sidebar=yes&bg=no".format(day) for day
        in ["24", "25", "26"]])
    pass
