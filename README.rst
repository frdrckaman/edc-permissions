|pypi| |travis| |codecov| |downloads|

edc-permissions
---------------

Simple classes for setting group permissions required for Edc deployments.


To add the default groups and permissions run the management command:

.. code-block:: python

    python manage.py update_edc_permissions


**Default Groups**

The default groups are required for the normal operation of an EDC deployment. The default groups are:

* ``ACCOUNT_MANAGER``: members may add/change and delete user accounts
* ``ADMINISTRATION``: members may view the Administration page
* ``AUDITOR``: members may view all forms but have no add/change permissions.
* ``CLINIC``: members may add/edit/delete all CRFs, Requisitions, Actions and other required clinic trial data entry forms. They may also view the Requisition page of the Lab section;
* ``EVERYONE``: members may access the EDC;
* ``LAB``: members may perform all functions in the Lab section (Edit requisitions, receive, process, pack, manage manifests, etc);
* ``PHARMACY``: 
* ``PII``: members may view all personally identifiable data and edit forms that manage such data (Screening, Consents, Patient registration);
* ``PII_VIEW``: members may view personally identifiable data but have no add/edit permissions for any of the forms that store such data.


**Default membership for Clinical staff**:

* ``EVERYONE``
* ``ADMINISTRATION``
* ``CLINIC``
* ``PII``

**Default membership for Laboratory technicians**:

* ``EVERYONE``
* ``ADMINISTRATION``
* ``LAB``
* ``PII_VIEW``

**Default membership for Auditors**:

* ``EVERYONE``
* ``ADMINISTRATION``
* ``AUDITOR``
* ``PII_VIEW``


** Permissions **

Permissions use Django's permission framework,  therefore, all permissions are linked to some model.

Permissions don't always naturally link to a model. In such cases, a dummy model is created. For example, with Navigation bars from `edc_navbar`. Permissions to follow an item on a navigation bar are associated with model `edc_navbar.Navbar`. A similar approach is used for `listboard` permissions using `edc_dashboard.Dashboard`.



.. |pypi| image:: https://img.shields.io/pypi/v/edc-permissions.svg
    :target: https://pypi.python.org/pypi/edc-permissions
    
.. |travis| image:: https://travis-ci.com/clinicedc/edc-permissions.svg?branch=develop
    :target: https://travis-ci.com/clinicedc/edc-permissions
    
.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-permissions/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/clinicedc/edc-permissions

.. |downloads| image:: https://pepy.tech/badge/edc-permissions
   :target: https://pepy.tech/project/edc-permissions
 