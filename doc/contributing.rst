.. _contributing:

Contributing
============

Expert knowledge is not needed to contribute to *statscollection*.
Every contribution is valuable, including:

- Reporting bugs and `issues <https://github.com/statscollection-dev/statscollection/issues>`_ that you encounter while using the package.
- Extending the documentation if the examples are incomplete or insufficient.
- Reviewing code written by others---you will learn a lot.
- Implementing new algorithms, if you're willing to read up on theory first.

Open source projects work best when people contribute actively.
Together, we can create great software for others to use.
This page describes how to contribute to the projects.
If you have trouble making a contribution, please create an `Issue <https://github.com/statscollection-dev/statscollection/issues>`_.

Creating a Pull Request
-----------------------

To make any kind of contribution, you will need to create a Pull Request on `GitHub <https://github.com/>`_.
Create a free account on GitHub if you have not done so already.
If you are unfamiliar with git, read the introductory chapers of the `git book <https://git-scm.com/book/en/v2>`_ or search for YouTube tutorials.
Below is a list explaining the steps needed to create a pull request, a terminal session is recorded below.

1. Fork the `statscollection <https://github.com/statscollection-dev/statscollection>`_ repository on GitHub. 
   This copies the project on your GitHub profile.
#. Clone the fork to your local computer using ``git clone https://github.com/<YOUR_NAME>/statscollection.git``.
   This downloads the files to your computer.
#. Add ``statscollection-dev/statscollection`` as a remote using ``asdf``.
   This allows you to fetch the lastest changes from the main repository, so you don't fall behind.
#. Create a feature branch.
#. Make changes to the software, perform linting and run the tests.
#. Commit your changes.
#. Push the changes.
#. Create a pull request.

If you make significant contributions, you will be invited to join the development team.
If you have made significant contributions but have not be invited, feel free to ask.

Terminal session for a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is a terminal session for a Pull Request.
Start by cloning the project to your GitHub account, downloading the files and adding a remote.

.. code-block:: console

   $ git clone https://github.com/<YOUR_NAME>/statscollection.git
   $ cd statscollection
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
   $ git push origin --set-upstream my_feature_branch


Documentation contributions
---------------------------

Documentation contributions are arguably the most important contributions!

1. Fork and clone the `statscollection <https://github.com/statscollection-dev/statscollection>`_ repository on GitHub. 
#. Install *sphinx-autobuild* via ``pip install sphinx-autobuild`` if you haven't.
#. Create a using ``git checkout -b my_feature_branch``.
#. In the ``statscollection`` directory, type ``sphinx-autobuild doc/ html/ -a -E --open-browser --watch .``
#. Edit files, make sure the documentation renders as expected.
#. Stage the changed files ``git add changed_file1.rst changed_file2.rst``.
#. Create a commit message ``git commit -m "description of changes"``.
#. Go to your fork ``https://github.com/<YOUR_NAME>/statscollection`` and create a Pull Request.

Building the docs
~~~~~~~~~~~~~~~~~

Docs may be built the ``sphinx-autobuild`` command.

.. code-block:: console

   $ sphinx-autobuild doc/ html/ -a -E --open-browser --watch .
   
   
Alternatively, the *sphinx-autobuild* package lets you continually build the documentation as you work.
   
.. code-block:: console

   $ sphinx-autobuild doc/ html/ -a -E --open-browser --watch .


Code contributions
------------------

Code contributions are important.

1. How to use ``black``.
#. How to test the code.
#. How to make a pull request.

Testing
~~~~~~~

.. code-block:: console

   $ pytest . --doctest-modules
   

Timing
~~~~~~

.. code-block:: console

   In [1]: %lprun -f Sample._fit_item_with_replacement timetest(n=10000)

Linting
~~~~~~~

TODO

.. code-block:: console

   $ black .



Building and deploying
----------------------

Developer notes go here.


