import grok

from raptus.mailcone.rules.factories import BaseFactoryCondition
from raptus.mailcone.rules.interfaces import IConditionItemFactory

from raptus.mailcone.rules_missingmail import _
from raptus.mailcone.rules_missingmail import interfaces
from raptus.mailcone.rules_missingmail.contents import MissingMailItem



class MissingMailFactory(BaseFactoryCondition):
    grok.name('raptus.mailcone.rules.missingmail')
    grok.implements(IConditionItemFactory)
    
    
    title = _('Missing mails')
    description = _('check of missing mails')
    form_fields = grok.AutoFields(interfaces.IMissingMailItem)
    ruleitem_class = MissingMailItem


    def box_output(self):
        re = super(MissingMailFactory, self).box_output()
        for i in re:
            if i['id'] is 'match':
                i['title'] = self._translate(_('missing'))
            if i['id'] is 'not_match':
                i['title'] = self._translate(_('nothing missing'))
        return re