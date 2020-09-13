class MyModelChoices(Enum):
   First = 'First'
   Second = 'Second'
   Third = 'Third'

class ChoicesColumn(tables.Column):
    def __init__(self, choices, attrs=None, **extra):
        self.choices = choices
        self.choices.insert(0, ('', '------'))
        kwargs = {'orderable': False, 'attrs': attrs}
        kwargs.update(extra)
        super(ChoicesColumn, self).__init__(**kwargs)

    def render(self, value, bound_column):
        select = forms.ChoiceField(choices=self.choices)
        return select.widget.render(bound_column.name, value)