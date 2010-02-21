from nose.tools import assert_true, assert_equal

from turbo_scrape.tests import TestController

from turbo_scrape.lib.scrape import *

class TestRootController(TestController):
    """The catch with this sample is that normally we functional test via WebTest
    <http://turbogears.org/2.1/docs/main/Testing/index.html>. This fakes out some of the WSGI stack
    so we don't actually need a webserver up.
    
    And here is where our demo app diverges from current (2009-2010) community practices,
    and uses scrape <http://zesty.ca/scrape/>. But this means we need an instance of paster server
    working.
    
    In fact, you are going to have to run serve at the same time as running nose. Like, for example,
    in another terminal window.
    """
    def test_index(self):
        s.go("http://localhost:8080/contacts")
        d = s.doc
        t = d.first("title")
        assert_equal("Turbogears Admin System - Contact Listing", t.text, 'did not go to the contact listing page')
        #assert_equal provided by nose.tools. <http://somethingaboutorange.com/mrl/projects/nose/doc/module_nose.tools.html>
    
    
    def test_new_to_new(self):
        """clicking on New Contact should take you to the New Contact Page"""
        s.go("http://localhost:8080/contacts")
        s.follow("New")
        assert_equal("http://localhost:8080/contacts/new", s.url)
    
