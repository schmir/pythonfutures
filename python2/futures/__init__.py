# Copyright 2009 Brian Quinlan. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Execute computations asynchronously using threads or processes."""

__author__ = 'Brian Quinlan (brian@sweetapp.com)'

from futures._base import (FIRST_COMPLETED,
                           FIRST_EXCEPTION,
                           ALL_COMPLETED,
                           CancelledError,
                           TimeoutError,
                           Future,
                           Executor,
                           wait,
                           as_completed)
from futures.process import ProcessPoolExecutor
from futures.thread import ThreadPoolExecutor
