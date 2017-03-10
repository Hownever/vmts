# -*- coding: utf-8 -*-

import platform
import os

# Platform

pre_platform = 0x00 if 'windows' in platform.platform().lower() else 0x01
pSlash = '\\' if pre_platform == 0x00 else '/'

# Pre_define

pre_define_conf_base_dir = pSlash.join(['', '..', 'conf', ''])
basic_lib_dir = os.path.dirname(__file__)
