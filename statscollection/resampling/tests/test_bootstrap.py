#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:31:04 2019

@author: tommy

"""

import pytest
import numpy as np
import pandas as pd
from statscollection.resampling import bootstrap_function


class TestBootstrapStatistic:
    def test_1D_input_general(self):
        """
        Test functionality on 1D inputs.
        """

        # Simple function to bootstrap, work on all valid data types
        function = lambda arr: arr[0]

        data = [[0, 1], [1, 1], [1, 2]]

        num_bootstraps = 99
        bs = bootstrap_function(
            data, function, num_bootstraps=num_bootstraps, random_state=42
        )

        assert len(bs) == num_bootstraps

    @pytest.mark.parametrize("data_type", [list, np.array, pd.Series])
    def test_1D_input(self, data_type):
        """
        Test functionality on 1D inputs.
        """

        # Simple function to bootstrap, work on all valid data types
        function = lambda arr: sum(arr)

        data = data_type([1, 2, 2])

        num_bootstraps = 99
        bs = bootstrap_function(
            data, function, num_bootstraps=num_bootstraps, random_state=42
        )

        assert len(bs) == num_bootstraps

    @pytest.mark.parametrize("data_type", [np.array, pd.DataFrame])
    def test_2D_input(self, data_type):
        """
        Test functionality on 1D inputs.
        """

        # Simple function to bootstrap, work on all valid data types
        function = lambda arr: sum(arr)

        def function(data):
            if isinstance(data, pd.DataFrame):
                data = data.values
            return np.dot(data[:, 0], data[:, 1])

        data = data_type([[0.2, 1], [0.2, 1], [0.2, 2], [0.8, 2]])

        num_bootstraps = 99
        bs = bootstrap_function(
            data, function, num_bootstraps=num_bootstraps, random_state=42
        )

        assert len(bs) == num_bootstraps


def test_bootstrap():
    pass


def test_dataset():
    pass


if __name__ == "__main__":
    import pytest

    pytest.main(
        args=[".", "--doctest-modules", "-v", "--disable-warnings", "--capture=sys"]
    )
