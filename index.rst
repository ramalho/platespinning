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
   :linenos:


Spinner with asyncio
--------------------

.. literalinclude:: spinner/spinner_asyncio.py
   :linenos:


Country flags (simple versions)
===============================


Sequential
----------

.. literalinclude:: countries/flags.py
   :linenos:


``concurrent.futures.ThreadPool``
---------------------------------

.. literalinclude:: countries/flags_threadpool.py
   :linenos:


``asyncio``
---------------------------------

.. literalinclude:: countries/flags_asyncio.py
   :linenos:


Charfinder
===============================


TCP Charfinder (telnet UI)
--------------------------

.. literalinclude:: charfinder/tcp_charfinder.py
   :linenos:


HTTP Charfinder (HTML UI)
-------------------------

.. literalinclude:: charfinder/http_charfinder.py
   :linenos:


