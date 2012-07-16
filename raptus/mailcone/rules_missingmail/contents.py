import grok
import datetime

from BTrees.OOBTree import OOBTree
from zope import component
from zope.annotation.interfaces import IAnnotations

from raptus.mailcone.mails.contents import Mail
from raptus.mailcone.rules import contents
from raptus.mailcone.rules_missingmail import _
from raptus.mailcone.rules_missingmail import interfaces



DATETIME_ANNOTATIONS_KEY = 'raptus.mailcone.rules_missingmail.datetime'



class MissingMailItem(contents.BaseActionItem):
    grok.implements(interfaces.IMissingMailItem)
    
    savedate = None
    periodic = ''
    
    def __init__(self):
        storage = IAnnotations(self)
        storage[DATETIME_ANNOTATIONS_KEY] = OOBTree()
    
    def apply_data(self, data, factory):
        super(MissingMailItem, self).apply_data(data, factory)
        self.savedate = datetime.datetime.now()
        storage = IAnnotations(self)
        storage[DATETIME_ANNOTATIONS_KEY] = OOBTree()
    
    @contents.process
    def process(self, charter):
        match = list()
        notmatch = list()
        
        if self.check(charter.mails):
            fake = Mail()
            for rel in self._relations('match'):
                copy = charter.copy(list(fake))
                rel.peer(self).process(copy)
        else:
            for rel in self._relations('not_match'):
                copy = charter.copy(charter.mails)
                rel.peer(self).process(copy)
        
    def test(self, mail, factory):
        """ no tests for this rule item.
        """
        return _(self.test.__doc__)
        
    def check(self, mails):
        storage = IAnnotations(self)[DATETIME_ANNOTATIONS_KEY]
        customer = '__empty__'
        if self._v_customer is not None:
            customer = self._v_customer.id
        if customer not in storage:
            storage[customer] = self.savedate
        date = storage[customer]
        period = component.getUtility(interfaces.IPeriod, name=self.periodic)
        result = period.check(date, mails)
        storage[customer] = datetime.datetime.now()
        return result
        




