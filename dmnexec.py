#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
    Make process as daemon and detach him
    usage: arg - executable file for running
"""

from    subprocess import Popen
import os
import sys


def createDaemon():
    try:
        pid = os.fork()
    except OSError, e:
        raise Exception("%s [%d]" % (e.strerror, e.errno))

    if not pid:
        os.setsid()
    else:
        os._exit(0)

    import resource     # Resource usage information.

    maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
    if maxfd == resource.RLIM_INFINITY:
        maxfd = 1024

    # Iterate through and close all file descriptors.
    for fd in range(0, maxfd):
        try:
            os.close(fd)
        except OSError:  # ERROR, fd wasn't open to begin with (ignored)
            pass

    os.open("/dev/null", os.O_RDWR)  # standard input (0)

    # Duplicate standard input to standard output and standard error.
    os.dup2(0, 1)           # standard output (1)
    os.dup2(0, 2)           # standard error (2)
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1:]
        retCode = createDaemon()
        if not retCode:
            Popen(cmd)
        sys.exit(retCode)
    sys.exit(0)
