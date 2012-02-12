import grok
import datetime

from zope import component
from zope.schema import vocabulary

from raptus.mailcone.rules_missingmail import _
from raptus.mailcone.rules_missingmail import interfaces





class BasePeriod(grok.GlobalUtility):
    grok.implements(interfaces.IPeriod)
    grok.baseclass()
    
    title = ''
    hours = 0
    
    def check(self, lastentry, mails):
        if len(mails):
            return True
        return datetime.datetime.now() + datetime.timedelta(hours=self.hours) > lastentry



class HalfDaily(BasePeriod):
    grok.name('raptus.mailcone.rules_missingemail.halfdaily')
    title = _('12 hours')
    hours = 12

class Daily(BasePeriod):
    grok.name('raptus.mailcone.rules_missingemail.daily')
    title = _('daily')
    hours = 24
    
class Weekly(BasePeriod):
    grok.name('raptus.mailcone.rules_missingemail.weekly')
    title = _('weekly')
    hours = 168

class Monthly(BasePeriod):
    grok.name('raptus.mailcone.rules_missingemail.monthly')
    title = _('monthly')
    hours = 744

class Cronjob(BasePeriod):
    grok.name('raptus.mailcone.rules_missingemail.cronjob')
    title = _('Each cronjob')
    hours = 0
    
    def check(self, lastentry, mails):
        return len(mails)



register = vocabulary.getVocabularyRegistry().register
def vocabulary_periodic(context):
    terms = list()
    for name, period in component.getUtilitiesFor(interfaces.IPeriod):
        terms.append(vocabulary.SimpleTerm(value=name, title=period.title))
    return vocabulary.SimpleVocabulary(terms)
register('raptus.mailcone.rules_missingmail.periodic', vocabulary_periodic)




