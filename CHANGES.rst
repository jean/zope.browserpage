Changes
=======

4.1.1 (unreleased)
==================

- TBD

4.1.1 (2014-12-24)
==================

- Fix deprecated unittest methods.

- Add explicit support for Python 3.4.

- Add explicit support for PyPy.


4.1.0a1 (2013-02-22)
====================

- Add support for Python 3.3.


4.0.0 (2012-07-04)
===================

- When registering views, no longer pass the deprecated 'layer' agrument
  to ``zope.component.registerAdapter``.  Instead, pass ``(for_, layer)``
  as expected (forward-compatibility with ``zope.component`` 4.0.0).

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.


3.12.2 (2010-05-24)
===================

- Fix unit tests broken under Python 2.4 by the switch to the standard
  library ``doctest`` module.


3.12.1 (2010-04-30)
===================

- Prefer the standard library's ``doctest`` module to the one from
  ``zope.testing``.


3.12.0 (2010-04-26)
===================

- Move the implementation of ``tales:expressiontype`` here from
  ``zope.app.pagetemplate``.


3.11.0 (2009-12-22)
===================

- Move the named template implementation here from ``zope.app.pagetemplate``.


3.10.1 (2009-12-22)
===================

- Depend on the ``untrustedpython`` extra of ``zope.security``, since we
  import from ``zope.pagetemplate.engine``.


3.10.0 (2009-12-22)
===================

- Remove the dependency on ``zope.app.pagetemplate`` by moving
  ``viewpagetemplatefile``, ``simpleviewclass`` and
  ``metaconfigure.registerType`` into this package.


3.9.0 (2009-08-27)
==================

- Initial release. This package was split off from ``zope.app.publisher``.
