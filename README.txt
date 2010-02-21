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


OK, now we have our models all ready - cool. First, we want to check to see if
our Contacts really did get created. We'll use CatWalk for that.
<http://code.google.com/p/tgtools/wiki/Catwalk>
-------------------------------------------------------------

<added CatWalk to UI per instructions above. Hack Hack Hack...>

Catwalk depends on the auth stuff being installed and up. Our application doesn't require this,
so we need to create our own unsecured CatWalk controller (in spite of what the Catwalk docs say...):

This really isn't a good idea, but for this sample it's OK. see
<http://groups.google.com/group/turbogears/browse_thread/thread/d4133a16c5221d26/5950c7904f3cb665?lnk=gst&q=tg2+catwalk#>
for some more discussion on this topic.

class UnSecuredCatwalk(Catwalk):
    allow_only = None

ALSO, you want to mount it in the RootController with:

catwalk = UnSecuredCatwalk( turbo_scrape.model, DBSession)

instead of what the CatWalk documentation says.
<http://turbogears.org/2.1/docs/main/QuickStart.html>


#14: paster serve development.ini #and visit http://localhost:8080/catwalk in your browser
