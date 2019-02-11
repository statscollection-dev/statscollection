#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Online
======

Online algorithms are algorithms which process a data stream of unknown length.
These algorithms become relevant when data is too large to fit into memory.


Overview
--------

.. currentmodule:: statscollection.online 


The following classes are available for online computations on data streams, i.e. any iterable object in Python.

.. autosummary::
   :nosignatures:
   :toctree:

   ~statscollection.online.classes.Mean
   ~statscollection.online.classes.Min
   ~statscollection.online.classes.Max
   
   
Online algorithms for sampling.

.. autosummary::
   :nosignatures:
   :toctree:

   ~statscollection.online.sampling.Sample
   

Tutorial
--------

The classes in this module share a common api, illustrated in the following example.

.. doctest:: python

    >>> from statscollection.online import Mean
    >>> mean = Mean().fit(2.0)  # Fit a single item
    >>> print(mean.evaluate())
    2.0
    >>> mean = mean.fit(iter([5.0, 2.0]))  # Fit an iterable object
    >>> print(mean.evaluate())
    3.0

It's possible to...

.. doctest:: python

    >>> for result in Mean().yield_from(iter([1.0, 3.0, 5.0])):
    ...     print(result)
    1.0
    2.0
    3.0
    
.. code-block:: python
   
    >>> print('hello world')
    hello world



"""
from statscollection.online.classes import Mean, Max, Min
from statscollection.online.sampling import Sample

Mean = Mean
Max = Max
Min = Min
Sample = Sample
