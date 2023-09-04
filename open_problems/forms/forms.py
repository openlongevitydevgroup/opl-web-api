from django import forms


class CreateRelationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        data = kwargs.pop("data", None)
        super(CreateRelationForm, self).__init__(*args, **kwargs)

        if data:
            self.fields["parent_question"].choices = data

    parent_question = forms.ChoiceField()
