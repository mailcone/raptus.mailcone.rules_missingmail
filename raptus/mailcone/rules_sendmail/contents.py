
import grok

from zope import component

from raptus.mailcone.settings.interfaces import ISMTPLocator

from raptus.mailcone.rules import contents
from raptus.mailcone.rules_sendmail import _
from raptus.mailcone.rules_sendmail import interfaces





class SendMailItem(contents.BaseActionItem):
    grok.implements(interfaces.ISendMailItem)
    
    # take only a single email address at the moment
    mail_addrs = ''
    subject = ''
    message = ''
    
    @contents.process
    def process(self, charter):
        for mail in charter.mails:
            self.send(mail)

    def test(self, mail, factory):
        try:
            self.send(mail)
            mapping = dict(factory=factory.title, title=self.title, addrs=self.mail_addrs)
            msg = 'Rule <${factory}@${title}> successfully send email(s) to  ${addrs}'
            return self.translate(_(msg, mapping=mapping))
        except Exception, e:
            return str(e)
    
    def send(self, mail):
        sender = component.getUtility(ISMTPLocator)()
        sender.send(self.message, self.subject, self.mail_addrs)




