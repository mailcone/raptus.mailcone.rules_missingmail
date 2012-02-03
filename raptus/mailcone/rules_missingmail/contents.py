import grok

from zope import component


from raptus.mailcone.rules import contents
from raptus.mailcone.rules_missingmail import _
from raptus.mailcone.rules_missingmail import interfaces





class MissingMailItem(contents.BaseActionItem):
    grok.implements(interfaces.IMissingMailItem)
    
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




