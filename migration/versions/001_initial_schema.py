from sqlalchemy import *
from migrate import *

metadata = MetaData(migrate_engine)
contacts_table = Table("contacts", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("first_name", Text, unique=True),
                    Column("last_name", Text),
                    Column("email", Text, unique=True)
                    )
def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    contacts_table.create()

def downgrade():
    # Operations to reverse the above upgrade go here.
    contacts_table.drop()
