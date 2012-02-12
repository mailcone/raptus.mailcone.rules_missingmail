from zope import schema
from zope import interface

from raptus.mailcone.rules import interfaces

from raptus.mailcone.rules_missingmail import _





class IMissingMailItem(interfaces.IConditionItem):
    """ check of missing mails
    """
    savedate = interface.Attribute('Last datetime where this item was saved')
    
    periodic = schema.Choice(title=_('Periodic'),
                             vocabulary='raptus.mailcone.rules_missingmail.periodic',
                             required=True)



class IPeriod(interface.Interface):
    
    title = interface.Attribute('name of this period')
    
    def check(self, lastentry, mails):
        """ calculate the with the lastentry date and
            time now the difference and return True or False.
        """







