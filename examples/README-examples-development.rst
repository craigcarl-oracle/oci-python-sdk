====================
Examples Development
====================

Getting Started
===============
Please consult the `Development README`__ for instructions on setting up your development environment.

__ https://github.com/oracle/oci-python-sdk/blob/master/README-development.rst


Style Guide
===========

Examples should be -

* Runnable
* Atomic and implemented as a module

  * A module should be limited to, at most, a single resource type.
  * The module should import other examples as required to be runnable.

* Be over-commented

  * The examples should be consumable by users of all skill levels.
  * Include a docstring.
  * Include links to the `API reference`__ for the API.

__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/index.html

* Be opinionated

  * An example should represent the best practise.

Tests
=====

Tests are encouraged but not yet required.