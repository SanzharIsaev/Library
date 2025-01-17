class NonRelRouter:

    nonrel_models = {'author', 'book'}

    def db_for_read(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def db_for_write(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def allow_migrate(self, _db, _app_label, model_name=None, **_hints):
        if _db == 'nonrel' or model_name in self.nonrel_models:
            return False
        return True