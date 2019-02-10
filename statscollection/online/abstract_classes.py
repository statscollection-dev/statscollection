#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Abstract base classes. These are never initialized.
"""

from collections import Iterable, Collection
from abc import ABC, abstractmethod
import numpy as np
import numbers


class OnlineStatistic(ABC):
    """
    An online statistic, which fits to data item-by-item.
    """

    def __init__(self):
        super().__init__()

    def fit(self, iterable_or_item):
        """
        Fit an iterable object or a single item.
        """

        assert isinstance(list([1, 2, 3]), Collection)
        assert isinstance(tuple([1, 2, 3]), Collection)
        assert isinstance(np.array([1, 2, 3]), Collection)

        # A collection, e.g. a list, tuple or np.array
        if isinstance(iterable_or_item, Collection):
            self._fit_collection(iterable_or_item)

        # Not a collection, but might still be iterable
        elif isinstance(iterable_or_item, Iterable):
            self._fit_iterable(iterable_or_item)

        # Not iterable
        elif isinstance(iterable_or_item, numbers.Number):
            self._fit_item(iterable_or_item)
        else:
            raise TypeError("The argument must be an iterable, or a number.")

        return self

    def _fit_collection(self, iterable):
        """
        Fit a collection.
        """
        self_fit_item = self._fit_item
        for item in iterable:
            self_fit_item(item)

    def _fit_iterable(self, iterable):
        """
        Fit an iterable by fitting every item sequentially.
        """

        self_fit_item = self._fit_item
        for item in iterable:
            self_fit_item(item)

    def yield_from(self, iterable):
        """
        Fit item-by-item and yield the sequential results.
        """
        self_fit = self.fit
        self_eval = self.evaluate
        for item in iterable:
            self_fit(item)
            yield self_eval()

    def return_from(self, iterable):
        """
        Fit item-by-item and yield the sequential results.
        """
        # A collection, e.g. a list, tuple or np.array
        if isinstance(iterable, Collection):
            return list(self.yield_from(iterable))

        # Not a collection, but might still be iterable
        elif isinstance(iterable, Iterable):
            return list(self.yield_from(iterable))

        else:
            raise TypeError("The argument must be an iterable, or a number.")

    @abstractmethod
    def evaluate(self, scalar):
        """
        Return the computed statistic.
        """
        pass

    @abstractmethod
    def _fit_item(self, item):
        """
        Fit a single item.
        """
        pass


class WeightedOnlineStatistic(OnlineStatistic):
    """
    An online statistic, which fits to data item-by-item and weight-by-weight.
    """

    def __init__(self):
        super().__init__()

    def fit(self, iterable_or_item, weights_or_weight):
        """
        Fit an iterable object or a single item. Weights must be passed too.
        """
        if isinstance(iterable_or_item, Iterable):
            self._fit_iterable(iterable_or_item, weights_or_weight)
        else:
            self._fit_item(iterable_or_item, weights_or_weight)

        return self

    def _fit_iterable(self, iterable, weights):
        """
        Fit an iterable by fitting every item and weight sequentially.
        """
        for item, weight in zip(iter(iterable), iter(weights)):
            self._fit_item(item, weight)

    def yield_from(self, iterable, weights):
        """
        Fit item-by-item and weight-by-weight and yield the sequential results.
        """
        for item, weight in zip(iter(iterable), iter(weights)):
            self.fit(item, weight)
            yield self.evaluate()

    @abstractmethod
    def evaluate(self, scalar):
        """
        Return the computed statistic.
        """
        pass

    @abstractmethod
    def _fit_item(self, item, weight):
        """
        Fit a single item and weight.
        """
        pass


if __name__ == "__main__":
    import pytest

    pytest.main(
        args=[".", "--doctest-modules", "-v", "--disable-warnings", "--capture=sys"]
    )
