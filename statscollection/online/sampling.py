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
import random
from abstract_classes import OnlineStatistic
from scipy import stats
import numpy as np


class Sample(OnlineStatistic):
    """
    Sample with equal probability from an iterable of unknown length.
    
    This algorithm maintains a sample of ``num_samples`` items as it iterates
    over a data stream of unknown length. This method of sampling is called 
    *reservoir sampling*. The algorithm guarantees that at any time, the 
    probability that any seen item is in the sample is equal. The algorithm 
    accomplishes this by decreasing the probability that an item in the sample 
    will be replaced by a newly seen item as it iterates over the data stream.
    
    Two different algorithms are implemented: one for sampling without
    replacement [1]_ and one for sampling with replacements [2]_. 
    
    Parameters
    ----------
    num_samples : int
        The number of samples to keep in the reservoir.
    replace : bool
        Whether or not sampling is with replacement. 

    Examples
    --------
    
    >>> import random
    >>> import numpy as np
    >>> random.seed(123)  # The algorithm is stochastic. Seed to reproduce.
    >>> np.random.seed(123)
    >>> stream = [1, 2, 3, 4, 5]
    
    When sampling without replacement, the reservoir will fill up gradually.
    
    >>> sampler = Sample(num_samples=3, replace=False)
    >>> for sample in sampler.yield_from(stream):
    ...   print(sample)
    [1]
    [1, 2]
    [1, 2, 3]
    [4, 2, 3]
    [4, 2, 5]
    
    When sampling with replacement, the reservoir will fill up immediately.
    
    >>> sampler = Sample(num_samples=10, replace=True)
    >>> for sample in sampler.yield_from(stream):
    ...   print(sample)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    [2, 1, 1, 1, 2, 2, 1, 2, 1, 1]
    [2, 1, 3, 1, 3, 3, 1, 3, 1, 1]
    [4, 1, 3, 1, 3, 3, 1, 3, 4, 1]
    [4, 1, 3, 1, 3, 3, 5, 3, 5, 1]

    
    References
    ----------
    .. [1] Jeffrey S. Vitter. *Random sampling with a reservoir*.
           ACM Transactions on Mathematical Software (TOMS), 1985.
           doi>10.1145/3147.3165
    .. [2] Park, Byung-Hoon & Ostrouchov, George & Samatova, 
           Nagiza & Geist, Al. (2004). *Reservoir-Based Random Sampling with 
           Replacement from Data Stream*. 
           doi>10.1137/1.9781611972740.53. 

    """

    def __init__(self, num_samples=10, replace=False):
        self.num_samples = num_samples
        self.samples = []
        self.seen_items_ = 0
        # self.indices_ = list(range(num_samples))

        # Use different functions depending on whether we draw with replacement
        if replace:
            self._fit_item = self._fit_item_with_replacement
        else:
            self._fit_item = self._fit_item_without_replacement

    def _fit_item(self, item):
        err = "Fitting is dependent on whether sampling is with replacements."
        raise NotImplementedError(err)

    def _fit_item_without_replacement(self, item):
        self.seen_items_ += 1

        # If the reservoir is not filled up yet, append the item to the list
        if len(self.samples) < self.num_samples:
            self.samples.append(item)
        else:
            # Generate a random index to possibly insert into
            random_index = random.randrange(self.seen_items_)
            # If the generated value is lower enough, accept the item
            if random_index < self.num_samples:
                self.samples[random_index] = item

    def _fit_item_with_replacement(self, item):
        self.seen_items_ += 1

        # How many times to sample
        # TODO: Timing shows that ~90% of the time is spent below.
        # I must go back to the paper and implement the skipping algorithm.
        res = stats.binom(n=self.num_samples, p=1 / self.seen_items_).rvs(1)
        num_times = np.asscalar(res)

        # If the reservoir is not filled up yet, fill it up immediately
        if not self.samples:
            self.samples = [item] * self.num_samples
            return None

        else:

            # If no sample is the reservoir is to be replaced, return
            if num_times == 0:
                return None

            # Find random indices, and replace the reservoir items.
            # We use numpy since random.choices samples with replacement, which
            # is not what we want in this case.

            random_indices = random.sample(range(self.num_samples), k=num_times)
            for index in random_indices:
                self.samples[index] = item

    def evaluate(self):
        return self.samples


def main():
    import pytest

    pytest.main(
        args=[".", "--doctest-modules", "-v", "--disable-warnings", "--capture=sys"]
    )


def timetest(n):
    stream = iter(range(n))

    np.random.seed(123)
    random.seed(123)
    estimator = Sample(num_samples=n, replace=True)
    import collections
    import time

    st = time.perf_counter()

    for item in stream:
        estimator.fit(item)
        # print(estimator.evaluate())
        # print(collections.Counter(estimator.evaluate()))

    print(time.perf_counter() - st)


if __name__ == "__main__":
    main()

    timetest(n=1000)
