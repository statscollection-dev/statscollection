.. _contributing:

Contributing
============

  Clean code, high-quality documentation and clear contribution guidelines will attract proficient developers.
  
Statscollection aims to be extremely *accessible to contributors*.
Every meaningful contribution is welcome, this includes

- **Documentation fixes** - spellchecking, rewriting, clarifying, extending, etc.
- **Code reviews** - reviewing existing code, rewriting functions, improving algorithms, etc.
- **Code contributions** - extending sub-packages or *creating your own sub-package*.

Contributors may list their GitHub usernames or full names in the :ref:`contributors` section.
High-quality contributions will give membership to the `statscollection-dev <https://github.com/statscollection-dev>`_ GitHub organization.

This page explains how to create a pull request, how to contribute to the documentation, and how to contribute to the code.
If you have trouble making a contribution, please create an `Issue <https://github.com/statscollection-dev/statscollection/issues>`_.

Creating a Pull Request
-----------------------

In order to contribute, you have to create a pull request on `GitHub <https://github.com/>`_.
Begin by creating a free account on GitHub if you have not done so already.
If you are unfamiliar with git, read the introductory chapers of the `git book <https://git-scm.com/book/en/v2>`_ or search for YouTube tutorials.
Below is a list describing the steps needed to create a pull request.

1. Fork the `statscollection <https://github.com/statscollection-dev/statscollection>`_ repository on GitHub. 
   This copies the project to your GitHub profile.
#. Clone the fork to your local computer using ``git clone https://github.com/<YOUR_NAME>/statscollection.git``.
   This downloads the files to your computer.
#. Add ``statscollection-dev/statscollection`` as a remote named 
   *upstream* using ``git remote add upstream https://github.com/statscollection-dev/statscollection``.
   This allows you to fetch the latest changes from the main repository, 
   so you don't fall behind if the master branch is updated while you work.
#. Create a feature branch for your work with ``git checkout -b my_feature``
#. Make changes to the docs and software, perform linting, run the tests and build the docs.
#. Commit your changes.
#. Merge any new commits from the master with ``git pull upstream master``.
#. Push the changes to your fork using ``git push origin --set-upstream my_feature``.
#. Create a pull request from ``https://github.com/<YOUR_NAME>/statscollection``.
#. If you need to add more commits, simply commit, pull from upstream and push to your fork again.

.. tip::
   When a pull request is created, the code will be tested and built.
   To see the exact commands executed when the code is tested and built, 
   read the `.travis.yml <https://github.com/statscollection-dev/statscollection/blob/master/.travis.yml>`_ file
   in the main repository.


Terminal session for a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A terminal session with comments in presented below.
We start by cloning the project to our GitHub account, downloading the files and adding a remote.

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


Code ideas
~~~~~~~~~~

TODO

.. code-block:: console

   $ black .


