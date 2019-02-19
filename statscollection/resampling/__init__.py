#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Resampling
==========

Docs go here.

>>> import numpy as np
>>> from statscollection.resampling import bootstrap_function
>>> sleep = np.array([7.07, 6.99, 8.49, 7.67, 6.95, 7.64, 8.03])
>>> medians = bootstrap_function(sleep, np.median, num_bootstraps=100, random_state=42)
>>> ans = np.quantile(medians, q=[0.05, 0.95], interpolation='linear')
>>> print(ans)
[6.99... 8.03...]
>>> means = bootstrap_function(sleep, np.mean, num_bootstraps=1000, random_state=42)
>>> ans = np.quantile(means, q=[0.01, 0.99], interpolation='linear')
>>> print(ans)
[7.13... 8.03...]



"""
from statscollection.resampling.bootstrap import bootstrap_function

bootstrap_function = bootstrap_function
