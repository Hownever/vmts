# -*- coding: utf-8 -*-

import psutil
import platform

def get():
    static = dict()

    static = {
        "base": {
            "python": {
                "version": platform.python_version(),
                "implementation": platform.python_implementation()
            },
            "platform": {
                "system": platform.uname()[0],
                "release": platform.uname()[2],
                "version": platform.uname()[3],
                "processor": platform.uname()[-1]
            },
            "os": {
                "host_name": platform.node(),
                "libc_version": platform.libc_ver()
            }
        }

    }

    return static