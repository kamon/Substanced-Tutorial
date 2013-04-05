=====================================
1: Project Start With Scaffolds
=====================================

Pyramid provides a facility called "scaffolds" that let you quickly
generate the basics of a Pyramid application.

Objectives
==========

- Use ``pcreate`` to see what scaffolds are available.

- Create and install a sample project using the Sustance D scaffold.

Steps
=====

#. See the usage for ``pcreate``:

   .. code-block:: bash

    (myenv)$ pcreate --help

#. List the available scaffolds:

   .. code-block:: bash

    (myenv)$ pcreate --list

#. Make a new Python project called ``directoryapp`` using ``substanced``:

   .. code-block:: bash

    (myenv)$ pcreate -s substanced directoryapp


#. Visit that project and see the project contents:

   .. code-block:: bash

    (myenv)$ cd directoryapp; ls

#. Install your new project:

   .. code-block:: bash

    (myenv33)$ python setup.py develop

#. Run the WSGI application with:

   .. code-block:: bash

    (myenv)$ pserve development.ini

#. Open ``http://127.0.0.1:6543/`` in your browser.

