import grok

from raptus.mailcone.rules.wireit import RuleBoxEditForm





class RuleBoxEditForm(RuleBoxEditForm):
    grok.name('wireit_edit_raptus_mailcone_missing_email')
    
    @property
    def tabs(self):
        tabs = super(RuleBoxEditForm, self).tabs
        for tab in list(tabs):
            if tab.get('id') in ('ui-tabs-overrides', 'ui-tabs-verify',):
                tabs.remove(tab)
        return tabs