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
