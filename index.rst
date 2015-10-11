.. Plate Spinning documentation master file, created by
   sphinx-quickstart on Sat Jun 20 06:22:29 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Plate Spinning's documentation!
==========================================

.. contents::

Spinner
=======

Spinner with thread
-------------------

.. literalinclude:: spinner/spinner_thread.py
    :language: Python3
    :linenos:


Spinner with asyncio (``yield`` version)
----------------------------------------

.. literalinclude:: spinner/spinner_yield.py
    :language: Python3
    :linenos:


Spinner with asyncio (``await`` version)
----------------------------------------

.. literalinclude:: spinner/spinner_await.py
    :language: Python3
    :linenos:

Country flags (simple versions)
===============================


Sequential
----------

.. literalinclude:: countries/flags.py
    :language: Python3
    :linenos:


``concurrent.futures.ThreadPool``
---------------------------------

.. literalinclude:: countries/flags_threadpool.py
    :language: Python3
    :linenos:


``asyncio``
---------------------------------

.. literalinclude:: countries/flags_asyncio.py
    :language: Python3
    :linenos:


Charfinder
===============================


TCP Charfinder (telnet UI)
--------------------------

.. literalinclude:: charfinder/tcp_charfinder.py
    :language: Python3
    :linenos:


HTTP Charfinder (HTML UI)
-------------------------

.. literalinclude:: charfinder/http_charfinder.py
    :language: Python3
    :linenos:
