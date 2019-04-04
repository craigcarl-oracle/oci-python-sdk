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

* Executable
* Atomic and implemented as a module

  * A module should be limited to, at most, a single resource type.
  * A module should implement a single architecture.

    * See the VCN examples.
  * A module should import other examples as required.

* Easily consumable by users of all skill levels

  * Examples should be over-commented.
  * Logging should be used be aggressively.
  * Functions should always include a docstring.
  * Module names should be descriptive.
  * Include links to the `API reference`__ for the API.
  * With exceptions for above examples should conform to PEP8.

__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/index.html


* Be opinionated

  * An example should represent the best practise.

    * Python 2.* compatibility is neither required nor encouraged.

Tests
=====

Tests are encouraged but not yet required.