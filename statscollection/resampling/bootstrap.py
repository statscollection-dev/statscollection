#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bootstrapping
"""

import numpy as np
import pandas as pd
from collections.abc import Collection


def resample_dataset(data, size, p):
    """
    Resample a data set.
    """
    if isinstance(data, np.ndarray):

        num_obs, num_dims = data.shape
        index = np.random.choice(np.arange(num_obs), size=size, replace=True, p=p)
        return data[index, :]

    elif isinstance(data, pd.DataFrame):

        num_obs, num_dims = data.shape
        index = np.random.choice(np.arange(num_obs), size=size, replace=True, p=p)
        return data.iloc[index, :]

    return data.iloc[index, :]


def resample_collection(data, size, p):
    """
    Resample a data set.
    """
    if isinstance(data, np.ndarray):
        assert data.ndim == 1
        return np.random.choice(data, size=size, p=p)

    elif isinstance(data, pd.Series):

        num_obs = len(data)
        index = np.random.choice(np.arange(num_obs), size=size, replace=True, p=p)
        return data.iloc[index]

    elif isinstance(data, Collection):

        num_obs = len(data)
        index = np.random.choice(np.arange(num_obs), size=size, replace=True, p=p)

        return type(data)([data[i] for i in index])


def bootstrap_function(
    data, function, sample_size=None, num_bootstraps=999, p=None, random_state=None
):
    """
    Bootstrap a function over a data set.
    
    
    Parameters
    ----------
    data : list, ndarray, Series or Dataframe
        A collection of observations. If a list, 1-D array-like or Series is given,
        the entries are interpreted as the samples. If a DataFrame is given, each row
        represents a sample. If a 2-D ndarray is given, it's assume to the of shape
        (num_obs, num_dims).
    function : str
        A function of a single parameter, of the same type as `data`. The return value
        of the function is appended to a list, so functions returning several numbers or
        arbitrary objects is possible.
    sample_size : str
        The second parameter.
    num_bootstraps : str
        The second parameter.
    p : 1-D array-like, optional
        The probabilities associated with each sample in `data`.
        If not given, the sample assumes a uniform distribution over all
        entries in `data`.
    random_state : int
        Random seed.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/
    
    
    Examples
    --------
    >>> import numpy as np
    >>> from statscollection.resampling import bootstrap_function
    """

    # -------------------------------------------------------------------
    # ---------- PROCESS AND VALIDATE THE INPUTS ------------------------
    # -------------------------------------------------------------------
    if isinstance(data, np.ndarray) and data.ndim in (1, 2):
        dimensionality = data.ndim
    elif isinstance(data, pd.Series):
        dimensionality = 1
    elif isinstance(data, pd.DataFrame):
        dimensionality = 2
    elif isinstance(data, Collection):
        dimensionality = 1
    else:
        raise TypeError(
            "Parameter `data` must be a Collection, np.ndarray of dimensionality 1 or 2, pd.Series or pd.Dataframe"
        )

    if random_state is not None:
        np.random.seed(random_state)

    if sample_size is None:
        sample_size = len(data)

    # -------------------------------------------------------------------
    # ---------- PROCESS AND VALIDATE THE INPUTS ------------------------
    # -------------------------------------------------------------------
    results = []

    for bootstrap_sample in range(num_bootstraps):

        # Draw a sample, where the logic is based on the dimensinality of the data
        if dimensionality == 2:
            sample = resample_dataset(data, size=sample_size, p=p)
        else:
            sample = resample_collection(data, size=sample_size, p=p)
            # sample = np.random.choice(data, size=sample_size, p=p)

        results.append(function(sample))

    return results


def bootstrap_dataset_1D(data, sample_size=None, num_bootstraps=999, p=None):
    """
  Bootstrap a 1D data set.
  """

    assert data.ndim == 1

    if sample_size is None:
        sample_size = data.size

    result = np.random.choice(
        data, size=(sample_size * num_bootstraps), replace=True, p=p
    )
    result = result.reshape(sample_size, num_bootstraps)
    assert result.shape[0] == sample_size
    assert result.shape[1] == num_bootstraps
    return result


def bootstrap_dataset(data, sample_size=None, num_bootstraps=999, p=None):
    """
  Bootstrap a data set of shape (num_obs, num_dims).
  """
    assert data.ndim == 2

    num_obs, num_dims = data.shape

    if sample_size is None:
        sample_size = num_obs

    result = np.empty(shape=(num_obs, num_dims, num_bootstraps), dtype=data.dtype)

    for dimension in range(0, num_dims):
        bootstrapped_dim = bootstrap_dataset_1D(
            data[:, dimension],
            sample_size=sample_size,
            num_bootstraps=num_bootstraps,
            p=p,
        )
        result[:, dimension, :] = bootstrapped_dim

    # of shape (num_obs, num_dims, num_bootstraps)
    return result


def bootstrap_aggregate(data, sample_size=None, num_bootstraps=999, p=None):
    pass


# choice(a, size=None, replace=True, p=None)


def main():
    import pytest

    pytest.main(
        args=[".", "--doctest-modules", "-v", "--disable-warnings", "--capture=sys"]
    )

    data = np.array([3, 5, 5, 4, 4, 4, 7])
    print(data.mean())

    bs = bootstrap_dataset_1D(data, sample_size=None, num_bootstraps=10)

    assert bs.shape[0] == len(data)

    print(bs)

    print(bs.mean(axis=0))

    print("-" * 99)

    data = np.array([[1, 0.2], [0, 0.8], [1, 0.8], [0, 0.8]])
    bs = bootstrap_dataset(data, sample_size=None, num_bootstraps=999)
    print(data)
    print(bs.shape)

    print(bs)

    print(bs.mean(axis=(0, 2)))


if __name__ == "__main__":
    main()
