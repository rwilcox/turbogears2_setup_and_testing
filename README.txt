Turbo-scrape shows how to test your application with the scrap framework
<http://zesty.ca/scrape/>.


Installation and Setup
======================

Install ``turbo-scrape`` using the setup.py script::

    $ cd turbo-scrape
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Then you are ready to go.


How I did what I did
===================

Started a Turbogears project...
#0: paster quickstart
#1: Grabbed scrape.py from <http://zesty.ca/scrape/> and put it in lib/

I'm not sure if these are normally required, but I needed them to get it working
on my system - RPW
-----------------------------------------------
#2: sudo easy_install zope.sqlalchemy
#3: sudo easy_install Babel
#4: sudo easy_install Catwalk 

Ok, back to normal setup
-----------------------------------------------
#5: paster setup-app development.ini
#6: paster serve development.ini


Then I started defining database migrations....
<http://turbogears.org/2.0/docs/main/DatabaseMigration.html>
#7: migrate create migration "create Contacts"
#8: migrate version_control sqlite:///devdata.db migration
#9: migrate script --repository=migration initial_schema

<hack hack hack on the file in migration/versions/...>
#10: migrate test migration sqlite:///devdata.db
#11: migrate upgrade sqlite:///devdata.db migration


Creating my models (we'll use sqlautocode to generate the initial one for contacts,
because I'm lazy. As this model migrates we might not want to use this approach, but
it's fine for our initial add of a table)
<http://turbogears.org/2.1/docs/main/Utilities/sqlautocode.html>.

We'll use the declarative way here, because (again) it's easy
-----------------------------------------------------------
#12: easy_install sqlautocode
#13: sqlautocode sqlite:///devdata.db -d -o turbo_scrape/model/contacts.py --tables=contacts

