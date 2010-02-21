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
#2: sudo easy_install zope.sqlalchemy
#3: sudo easy_install Babel
#4: sudo easy_install Catwalk 
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
