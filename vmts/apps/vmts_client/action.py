# -*- coding: utf-8 -*-

import commands
import os

class CommandAction(object):
    ''''''

    @classmethod
    def copy(cls, ):
        pass


    @classmethod
    def execute(cls, fp, params=None):
	fp = fp.split('\\n')[0] + '\n' + fp.split('\\n')[1]	
	if params:
            # todo
            pass

        # special callback
        def cpu_id(r):
	    return commands.getoutput(r'echo %s | grep -o "\w\{4\}-\w\{4\}-\w\{4\}-\w\{4\}"'%r)

        res = commands.getoutput(fp).split('\n')[0]
        if 'dennied' in res:
            os.system('chmod 775 {fp}'.format(fp=fp))
            res = commands.getoutput(fp)
	res = cpu_id(res)
	
        return res

