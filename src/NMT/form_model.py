from wtforms import Form, validators, StringField


class InputForm(Form):
    src_text = StringField(
        label='English Text',
        default='',
        validators=[validators.InputRequired()]
    )
