from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('sql','SQL'),('java','JAVA')]
class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
