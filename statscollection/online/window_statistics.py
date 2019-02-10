#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 07:51:36 2019

@author: tommy

https://github.com/jiecchen/StreamLib
https://en.wikipedia.org/wiki/Bloom_filter
https://polylogblog.wordpress.com/
https://stackoverflow.com/questions/2612648/reservoir-sampling
http://code.activestate.com/recipes/576930-efficient-running-median-using-an-indexable-skipli/
https://rhettinger.wordpress.com/2010/02/06/lost-knowledge/
https://epubs.siam.org/doi/pdf/10.1137/1.9781611972740.53
"""

import math
import functools
import random
import collections
from .abstract_classes import OnlineStatistic, WeightedOnlineStatistic


class WindowedMean(OnlineStatistic):
    """
    A windowed mean.

    Examples
    --------
    >>> 1 + 1
    2
    """

    def __init__(self, n=10):
        self.n = n
        self.window_length_ = 0
        self.sum_ = 0
        self.deque_ = collections.deque([])

    def _fit_item(self, item):
        self.window_length_ = min(self.window_length_ + 1, self.n)

        # Add the new value
        self.deque_.append(item)
        self.sum_ += item

        # Remove the past value
        if len(self.deque_) > self.n:
            removed = self.deque_.popleft()
            self.sum_ -= removed

    def evaluate(self):
        return self.sum_ / self.window_length_


class WindowedSample(OnlineStatistic):
    """
    A windowed sample.

    http://www.cs.umd.edu/~samir/498/vitter.pdf

    Examples
    --------
    >>> import random
    >>> random.seed(123)  # The algorithm is stochastic. Seed to reproduce.
    >>> stream = iter([5, 2, 3, 7, 4])
    >>> sampler = WindowedSample(num_samples=2)
    >>> for sample in sampler.yield_from(stream):
    ...   print(sample)
    [5]
    [5, 2]
    [3, 2]
    [3, 2]
    [4, 2]
    """

    def __init__(self, num_samples=10):
        self.num_samples = num_samples
        self.seen_items_ = 0
        self.samples = []

    def _fit_item(self, item):
        self.seen_items_ += 1

        # If the reservoir is not filled up yet, append the item to the list
        if len(self.samples) < self.num_samples:
            self.samples.append(item)
            # print(f'added, looks like {self.samples}')
        else:
            # Generate a random index to possibly insert into
            random_index = random.randrange(self.seen_items_)
            # print(f'Generated {random_index} range({0}, {self.i_ + 1})')
            # print(f'keeping if {random_index} < {self.n}')
            # If the generated value is lower enough, accept the item
            if random_index < self.num_samples:
                # Keep it
                # print(' keeping it')
                self.samples[random_index] = item

    def evaluate(self):
        return self.samples


class WindowedWeightedMean(OnlineStatistic):
    """
    A windowed weighted mean.

    Examples
    --------
    >>> 1 + 1
    2
    """

    def __init__(self, n=10, k=2):
        self.n = n
        self.k = k
        self.window_length_ = 0
        self.sum_ = 0
        self.deque_ = collections.deque([])

    def _fit_item(self, item):
        self.window_length_ = min(self.window_length_ + 1, self.n)

        # Remove the past value
        if len(self.deque_) >= self.n:
            removed = self.deque_.popleft()
            self.sum_ -= removed
            self.sum_ /= self.k

        # Add the new value
        self.deque_.append(item)
        self.sum_ += item * self.k ** (self.window_length_ - 1)

    def evaluate(self):
        # print(self.sum_, self.window_length_)
        sum_weights = (self.k ** (self.window_length_) - 1) / (self.k - 1)
        return self.sum_ / sum_weights


def main():
    import pytest

    pytest.main(
        args=[".", "--doctest-modules", "-v", "--disable-warnings", "--capture=sys"]
    )


if __name__ == "__main__":
    main()

    import itertools

    items = iter(range(50))
    sm = WindowedWeightedMean(n=10, k=2)

    for i in items:
        sm._fit_item(i)
        print(i, sm.evaluate(), sm.window_length_, sm.deque_)

    print("------")
    random.seed(123_456)
    items = list([random.randrange(10) for i in range(1_000_000)])
    sm = WindowedSample(num_samples=1000)
    import statistics

    for counter, i in enumerate(items):
        sm._fit_item(i)
        if counter % 10000 == 0:
            print(statistics.mean(sm.evaluate()))

    import statistics

    print(statistics.mean(items), statistics.mean(sm.evaluate()))
