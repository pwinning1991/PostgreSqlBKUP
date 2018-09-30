pgabackup
========


CLI for backing up for remote PostgreSQL databses locally or to AWS S3

Preparing for Devleopment
-------------------------


1.Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@guthub.com:example/pgbackup``
3. Fetch development dependencies: ``make install``

Usage
----

Pass in a full databse URL, the storage driver, and destination.

S3 Example w/ bucket name:

::
    $pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::
    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

::

    $ make

If virtualenv isn't active then use:

::
   $  pipenv run make


