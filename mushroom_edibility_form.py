from wtforms.validators import DataRequired,NumberRange
from wtforms.fields import FloatField,IntegerField
from flask_wtf import FlaskForm

class mushroom_edibility_form1(FlaskForm):
    capDiameter=IntegerField('Cap-Diameter:',validators=[DataRequired(message='The cap-diameter field is not filled'),NumberRange(min=0,max=1890,message= 'The cap-diameter is in between 0 to 1890')],render_kw={'min':'0','max':'1890','step':'1','inputmode':'numeric','placeholder':'Enter 0-1890','maxlength':'4'})

    capShape=IntegerField('Cap-Shape:',validators=[DataRequired(message='The cap-shape field is not filled'),NumberRange(min=0,max=6,message='The cap-shape is in between 0 to 6')],render_kw={'min':'0','max':'6','inputmode':'numeric','step':'1','placeholder':'Enter 0-6'})

    gillAttachment=IntegerField('Gill-Attachment:',validators=[DataRequired(message='The gill-attachment field is not filled'),NumberRange(min=0,max=6,message='The gill-attachment is in between 0 to 6')],render_kw={'min':'0','max':'6','inputmode':'numeric','step':'1','placeholder':'Enter 0-6'})

    gillColor=IntegerField('Gill-Color:',validators=[DataRequired(message='The gill-color field is not filled'),NumberRange(min=0,max=11,message= 'The gill-color is in between 0 to 11')],render_kw={'min':'0','max':'11','inputmode':'numeric','step':'1','placeholder':'Enter 0-11'})

    stemHeight=FloatField('Stem-Height:',validators=[DataRequired(message='The stem-height field is not filled'),NumberRange(min=0.0,max=4.0,message= 'The stem-height is in between 0.0 to 4.0')],render_kw={'min':'0.0','max':'4.0',"step":"0.1",'inputmode':'decimal','placeholder':'Enter 0.0-4.0'})

    stemWidth=IntegerField('Stem-Width:',validators=[DataRequired(message='The stem-width field is not filled'),NumberRange(min=0,max=3569,message= 'The stem-width is in between 0 to 3569')],render_kw={'min':'0','max':'3569','inputmode':'numeric','step':'1','placeholder':'Enter 0-3569'})

    stemColor=IntegerField('Stem-Color:',validators=[DataRequired(message='The stem-color field is not filled'),NumberRange(min=0,max=12,message= 'The stem-color is in between 0 to 12')],render_kw={'min':'0','max':'12','inputmode':'numeric','step':'1','placeholder':'Enter 0-12'})

    season=FloatField('Season:',validators=[DataRequired(message='The season field is not filled'),NumberRange(min=0.0,max=2.0,message= 'The season is in between 0.0 to 2.0')],render_kw={'min':'0.0','max':'2.0','inputmode':'decimal',"step":"0.1",'placeholder':'Enter 0.0 to 2.0'})

    