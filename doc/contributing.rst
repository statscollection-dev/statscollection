.. _contributing:

Contributing
============

  Clean code, high-quality documentation and clear contribution guidelines will attract proficient developers.

Statscollection aims to be extremely *accessible to contributors*.
Valuable contributions include:

- **Documentation fixes** - spell-checking, rewriting, clarifying, extending, etc.
- **Code reviews** - reviewing existing code, rewriting functions, improving algorithms, etc.
- **Code contributions** - extending sub-packages or *creating your own sub-package*.

Contributors may list their full name or GitHub username in the :ref:`contributors` section below.
Contributors providing high-quality content will be given membership to the `statscollection-dev <https://github.com/statscollection-dev>`_ GitHub organization.

This page explains how to create a pull request, how to contribute to the documentation, and how to contribute to the code.
In addition to the text below, the following resources might be useful:

- `Creating a Simple Github Pull Request <https://www.youtube.com/watch?v=rgbCcBNZcdQ>`_
- `How to Contribute to Open Source <https://opensource.guide/how-to-contribute/>`_
- `The git book <https://git-scm.com/book/en/v2>`_
- `Learn Git Branching <https://learngitbranching.js.org/>`_

.. tip::
   Do you know of any other good resources? **Create a pull request** and we'll add it.


If you have trouble making a contribution, please create an `Issue <https://github.com/statscollection-dev/statscollection/issues>`_ to get help.

Creating a Pull Request
-----------------------

In order to contribute, you have to create a pull request on `GitHub <https://github.com/>`_.
Begin by creating a free account on GitHub if you have not done so already.
Below is a list describing the steps needed to create a pull request.

1. Fork the `statscollection <https://github.com/statscollection-dev/statscollection>`_ repository on GitHub.
   This copies the project to your personal GitHub profile.
#. Clone the fork to your local computer by typing ``git clone https://github.com/<YOUR_NAME>/statscollection.git`` in the terminal (git bash if you're on Windows).
   This downloads the files to your computer.
#. Add ``statscollection-dev/statscollection`` as a remote named
   *upstream* by typing ``git remote add upstream https://github.com/statscollection-dev/statscollection``.
   This allows you to fetch the latest changes from the main repository,
   so you don't fall behind if the master branch is updated while you work on your feature branch.
#. Create a feature branch for your work with ``git checkout -b my_feature``
#. Make changes to the docs and software, perform linting, run the tests and build the docs.
   For more information about this, see the sections below.
#. Commit your changes with ``git add myfile.py`` and ``git commit -m "clear message"``.
#. Merge any new commits from the master with ``git pull upstream master``.
#. Push the changes to your fork using ``git push origin --set-upstream my_feature``.
#. Create a pull request from ``https://github.com/<YOUR_NAME>/statscollection``.
#. If you need to add more commits, simply commit, pull from upstream and push to your fork again.

.. tip::
   When a pull request is created, the code will be **tested and built** by Travis CI.
   To see the exact commands executed when the code is tested and built,
   read the `.travis.yml <https://github.com/statscollection-dev/statscollection/blob/master/.travis.yml>`_ file
   in the main repository.
   If your pull request fails on Travis CI, make the necessary changes and push a new commit to the same branch.


Terminal session for a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A terminal session with comments is presented below.
We start by cloning the project from our GitHub account, downloading the files and adding a remote.

.. code-block:: console

   $ git --version # git version 2.7.4
   $ git clone https://github.com/<YOUR_NAME>/statscollection.git
   $ cd statscollection # Change directory
   $ git remote add upstream https://github.com/statscollection-dev/statscollection.git

Create a feature branch for your changes, make changes, test and commit.

.. code-block:: console

   $ git fetch upstream master # Get the latest changes from the master
   $ git checkout -b my_feature_branch # Create a new branch for development
   $ <MAKE CHANGES> # Edit files, create new files, fix docs, etc
   $ pytest . --doctest-modules # Run the tests
   $ black . # Autoformat the code
   $ git add changed_file1.py changed_file2.py
   $ git commit -m "description of changes"
   $ git fetch upstream master # Get the latest changes from the master
   $ git push origin --set-upstream my_feature_branch


Documentation contributions
---------------------------

Documentation contributions are important contributions.
If you only change the documentation, there is no need to run code formatting and tests locally.
You should still build the documentation locally and verify that it looks good.

1. Fork and clone the `statscollection <https://github.com/statscollection-dev/statscollection>`_ repository on GitHub.
#. Install *sphinx-autobuild* via ``pip install sphinx-autobuild`` if you haven't.
   This is not a requirement, you can use the ``sphinx-build`` command manually as well.
#. Create a feature branch using ``git checkout -b my_feature_branch``.
#. In the ``statscollection`` directory, type ``sphinx-autobuild doc html -a -E --open-browser --watch .`` to start building docs automatically.
#. Edit files, make sure the documentation renders as expected.
#. Stage the changed files ``git add changed_file1.rst changed_file2.rst``.
#. Create a commit message ``git commit -m "description of changes"``.
#. Go to your fork ``https://github.com/<YOUR_NAME>/statscollection`` and create a Pull Request.

Building the docs
~~~~~~~~~~~~~~~~~

Docs may be built using the ``sphinx-build`` command.

.. code-block:: console

   $ sphinx-build doc html -a -E -W --keep-going -T


Alternatively, the *sphinx-autobuild* package lets you continually build the documentation as you work.

.. code-block:: console

   $ sphinx-autobuild doc html -a -E --open-browser --watch .


Code contributions
------------------

If you wish to contribute code, you have to

1. Run formatting on the code via the `black <https://black.readthedocs.io/en/stable/>`_ code formatter.
#. Write tests for the code, testing is done using `pytest <https://docs.pytest.org/en/latest/>`_.
#. Document the code well, this project uses `numpydoc docstrings <https://numpydoc.readthedocs.io/en/latest/format.html>`_.
#. Balance readability with performance.
   Readability has first priority, but if you `time the code <http://pynash.org/2013/03/06/timing-and-profiling/>`_ and identify bottlenecks, they should be optimized.


Testing
~~~~~~~

Test the code with `pytest <https://docs.pytest.org/en/latest/>`_.
The documentation will double as a test---but documentation does not replace testing.
Every algorithm implemented should be well tested.
This involves (1) unit tests, (2) testing against existing implementations and (3) property-based testing, if possible.

.. code-block:: console

   $ pytest . --doctest-modules


Timing
~~~~~~

Only optimize code that's actually slow.
While ``%timeit`` tests the speed of a function, the code may be timed line-by-line using the ``%lprun`` command in an Ipython console.
Using ``%lprun`` requires installation of the `line_profiler <https://github.com/rkern/line_profiler>`_ package.

The first line times the function, and the second line yields a line-by-line result.

.. code-block:: console

   In [1]: %timeit function_to_run(n=10000)

   In [2]: %lprun -f Class.function_to_time function_to_run(n=10000)

Linting
~~~~~~~

The project uses the `black <https://black.readthedocs.io/en/stable/>`_ code formatter.
Run black on the Python files before submitting a pull request.

.. code-block:: console

   $ black .


Building and deploying
----------------------

Developer notes go here.




Code contribution ideas
~~~~~~~~~~~~~~~~~~~~~~~

Below is a list of routines that would be nice to see implemented.

- Bootstrapping and resampling functions.
- Online statistics.
- Kernel density estimators (copy implementation from KDEpy).
- Kernel regression.
- Other nonparametric routines.
- Statistical tests, such as exact Mann–Whitney U test.
