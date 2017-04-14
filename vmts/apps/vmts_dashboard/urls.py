# -*- coding: utf-8 -*-

from handlers import index, device, task, user


urls = [
    (r'/', index.IndexHandler),
    (r'/login', index.LoginHandler),
    (r'/logout', index.LogoutHandler),
    (r'/device/(.*)', device.DeviceInfo),
    (r'/task/(.*)', task.TaskInfo),
    (r'/user/(.*)', user.UserInfo)
]