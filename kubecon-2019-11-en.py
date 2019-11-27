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
        "https://kccncna19.sched.com/2019-11-{}/overview?iframe=no&w=100%&sidebar=yes&bg=no".format(day) for day
        in ["18", "19", "20", "21"]])
    pass
