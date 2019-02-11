#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classes containing algorithms for online statistics.
"""
import functools
import math
from statscollection.online.abstract_classes import (
    OnlineStatistic,
    WeightedOnlineStatistic,
)


class Mean(OnlineStatistic):
    """
    The arithmetic mean.

    The arithmetic mean, or simly the mean or the average, is the first order
    moment of a probability denstiy function.

    Examples
    --------
    >>> stream = iter([1, 2, 3])
    >>> for mean in Mean().yield_from(stream):
    ...   print(mean)
    1.0
    1.5
    2.0
    >>> mean = Mean()
    >>> mean = mean.fit(1)
    >>> print(mean.evaluate())
    1.0
    """

    def __init__(self):
        self.n_ = 0
        self.mean_ = 0

    def _fit_item(self, item):
        self.n_ += 1
        self.mean_ += (item - self.mean_) / self.n_

    def evaluate(self):
        return self.mean_


class WeightedMean(WeightedOnlineStatistic):
    """
    The weighted arithmetic mean.

    More info here.

    """

    def __init__(self):
        self.w_ = 0
        self.mean_ = 0

    def _fit_item(self, item, weight=1):
        self.w_ += weight
        self.mean_ += ((item - self.mean_) / self.w_) * weight

    def evaluate(self):
        return self.mean_


class Max(OnlineStatistic):
    """
    The maximum.
    """

    def __init__(self):
        self.max_ = -float("inf")

    def _fit_item(self, item):
        self.max_ = max(self.max_, item)

    def evaluate(self):
        return self.max_


class Min(OnlineStatistic):
    """
    The minimum.
    """

    def __init__(self):
        self.min_ = float("inf")

    def _fit_item(self, item):
        self.min_ = min(self.min_, item)

    def evaluate(self):
        return self.min_


class GeometricMean(OnlineStatistic):
    """
    The geometric mean.

    Examples
    --------
    >>> GeometricMean().fit([6, 3, 8, 3]).evaluate()
    4.559014113909555
    >>> for m in GeometricMean().yield_from([1.02, 1.05, 1.08]):
    ...   print(m)
    1.02
    1.0348912986396204
    1.049714207933624
    >>> GeometricMean().fit([1.02, 1.05, 1.08]).evaluate()
    1.049714207933624

    """

    def __init__(self):
        self.neg_ = 0
        self.mean_log_ = Mean()

    def _fit_item(self, item):
        if item < 0:
            self.neg_ += 1
        self.mean_log_._fit_item(math.log(item))

    def evaluate(self):
        if self.neg_ % 2 == 0:
            return math.exp(self.mean_log_.evaluate())
        else:
            return -math.exp(self.mean_log_.evaluate())


class HarmonicMean(OnlineStatistic):
    """
    The harmonic mean.

    Examples
    --------
    >>> HarmonicMean().fit([4, 2, 3]).evaluate()
    2.7692307692307696
    """

    def __init__(self):
        self.n_ = 0
        self.reciprocal_sum_ = 0

    def _fit_item(self, item):
        self.n_ += 1
        self.reciprocal_sum_ += 1 / item

    def evaluate(self):
        return self.n_ / self.reciprocal_sum_


def naive_moment(data, p):
    import statistics

    m = statistics.mean(data)
    return sum((d - m) ** p for d in data)


@functools.lru_cache(maxsize=1024, typed=False)
def choose(n, k):
    if 2 * k > n:
        return choose(n, n - k)

    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


class CentralMoments(OnlineStatistic):
    """
    The central moments up to order `order_max`.

    See https://arxiv.org/pdf/1510.04923.pdf

    Examples
    --------
    >>> data = [1, 5, 3, 7]
    >>> for moment in CentralMoments(order_max=2).yield_from(data):
    ...   print(moment[2])
    0.0
    8.0
    8.0
    20.0
    >>> data = [3, 8, 5, 1, 9, 3]
    >>> for moment in CentralMoments(order_max=4).yield_from(data):
    ...   print((moment[3], moment[4]))
    (0.0, 0.0)
    (0.0, 78.125)
    (6.222222222222222, 80.22222222222223)
    (16.87500000000002, 312.078125)
    (-7.919999999999952, 604.5759999999998)
    (35.44444444444449, 640.486111111111)
    """

    def __init__(self, order_max=2):
        """

        Parameters
        ----------
        order_max : int
        """
        self.order_max = order_max
        self.n_ = 0
        self.mean_ = 0
        self.moments_ = {o: 0 for o in range(2, order_max + 1)}

    def _fit_item(self, item):
        """
        """
        self.n_ += 1
        delta = item - self.mean_
        self.mean_ += delta / self.n_

        self.moments_[2] += delta * (delta - (delta / self.n_))

        # Precompute delta / n to the power of k outside of the loop
        delta_div_k_powers = [(delta / self.n_) ** k for k in range(1, self.order_max)]

        for order in range(3, self.order_max + 1):

            # time is spent here
            elements = [
                choose(order, k) * delta_div_k_powers[k - 1] * self.moments_[order - k]
                for k in range(1, order - 1)
            ]

            # print([(delta / self.n_)**k for k in range(1, order-1)])
            # print(delta_div_k_powers)
            # print(elements)
            elements = sum(elements)

            self.moments_[order] += -elements + delta * (
                delta ** (order - 1) - (delta / self.n_) ** (order - 1)
            )
            # print(order)

    def evaluate(self):
        return self.moments_


class Variance(OnlineStatistic):
    """
    The arithmetic mean.

    The arithmetic mean, or simly the mean or the average, is the first order
    moment of a probability denstiy function.

    Examples
    --------
    >>> stream = iter([1, 2, 3])
    >>> for var in Variance().yield_from(stream):
    ...   print(var)
    0.0
    0.25
    0.666666666666...
    """

    def __init__(self):
        self.n_ = 0
        self.mean_ = 0
        self.var_ = 0

    def _fit_item(self, item):
        self.n_ += 1
        delta = item - self.mean_
        self.mean_ += delta / self.n_

        self.var_ += delta * (delta - (delta / self.n_))

    def evaluate(self):
        return self.var_ / self.n_


def iterate_paralell(iterable, statistics):
    pass


def main():
    import pytest

    pytest.main(
        args=[".", "--doctest-modules", "-v", "--disable-warnings", "--capture=sys"]
    )

    import random
    import time
    import matplotlib.pyplot as plt

    random.seed(123)

    if True:
        N = 10 ** 4

        mean = 1
        data = [mean]
        for i in range(N // 2):
            num = random.random()
            data.append(mean - num)
            data.append(mean + num)

        random.shuffle(data)

        st = time.perf_counter()
        means = list(Mean().yield_from(data))
        print(time.perf_counter() - st)
        print(means[-1])
        plt.plot(means, label="mean")

        st = time.perf_counter()
        means = list(Max().yield_from(data))
        print(time.perf_counter() - st)
        plt.plot(means)

        st = time.perf_counter()
        means = list(Min().yield_from(data))
        print(time.perf_counter() - st)
        plt.plot(means)

        st = time.perf_counter()
        variances = list(Variance().yield_from(data))
        print(time.perf_counter() - st)
        plt.plot(variances)

        # plt.scatter(list(range(N)), data, color='red', marker='x')

        plt.grid(True)
        plt.legend()
        plt.show()

    import time
    import random

    data = [random.random() for i in range(10 ** 5)]

    st = time.perf_counter()
    CentralMoments(order_max=5).fit(data)
    print(time.perf_counter() - st)

    """
[3] 0
[3, 8] 78.125
[3, 8, 5] 80.22222222222223
[3, 8, 5, 1] 312.078125
[3, 8, 5, 1, 9] 604.576
[3, 8, 5, 1, 9, 3] 640.4861111111112
    """


if __name__ == "__main__":
    main()
