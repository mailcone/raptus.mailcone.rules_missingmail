import grok

from raptus.mailcone.rules.factories import BaseFactoryAction
from raptus.mailcone.rules.interfaces import IActionItemFactory

from raptus.mailcone.rules_sendmail import _
from raptus.mailcone.rules_sendmail import interfaces
from raptus.mailcone.rules_sendmail.contents import SendMailItem



class SendMailFactory(BaseFactoryAction):
    grok.name('raptus.mailcone.rules.sendmail')
    grok.implements(IActionItemFactory)
    
    
    title = _('Send email')
    description = _('send a notification mail to a given address.')
    form_fields = grok.AutoFields(interfaces.ISendMailItem)
    ruleitem_class = SendMailItem
