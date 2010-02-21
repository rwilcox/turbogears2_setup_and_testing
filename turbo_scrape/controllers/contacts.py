from tgext.crud import CrudRestController
from turbo_scrape.model import DBSession
from turbo_scrape.model.contacts import Contact

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller, FormFiller, RecordFiller
from sprox.formbase import AddRecordForm

class ContactTable(TableBase):
    __model__ = Contact


class ContactTableFiller(TableFiller):
    __model__ = Contact


class ContactEditFiller(RecordFiller):
    __model__ = Contact

class ContactAddForm(AddRecordForm):
    __model__ = Contact


class ContactsController(CrudRestController):
    model = Contact
    table_filler = ContactTableFiller(DBSession)
    table = ContactTable(DBSession)
    new_form = ContactAddForm(DBSession)
    edit_form = ContactAddForm(DBSession)
    edit_filler = ContactEditFiller(DBSession)
