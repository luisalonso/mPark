from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from mParkCore.models import Professional, Team, Session, Post, Comment
from django.utils.translation import gettext as _

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    error_messages = {
        'duplicate_username': 'my custom error message'
    }

    class Meta:
        model = User
        fields = ('email', 'name', 'last_name', 'password1', 'password2')

    def save(self,commit = True):
        u = User.objects.filter(username=self.cleaned_data["email"])

        if u.exists():
            raise forms.ValidationError(_('This email is already in use..'),
                        code='unique_username')

        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            team = Team(name=self.cleaned_data['email'], text='Individual team')
            team.save()
            professional = Professional(user=user, profile='profesional', team=team, email=self.cleaned_data['email'], name=self.cleaned_data['name'], last_name=self.cleaned_data['last_name'])
            professional.save()

        return user

class AddSession(forms.ModelForm):
    phase_I_duration = forms.CharField(label="phase_I_duration", required=False,
    widget=forms.NumberInput(
    attrs={'type':'range'}))

    phase_II_duration = forms.CharField(label="phase_II_duration", required=False,
    widget=forms.NumberInput(
    attrs={'type':'range'}))

    phase_III_duration = forms.CharField(label="phase_III_duration", required=False,
    widget=forms.NumberInput(
    attrs={'data-slider-min': '0',
    'data-slider-max': '10',
    'data-slider-step': '1',
    'data-slider-value': 5}))

    phase_IV_duration = forms.CharField(label="phase_IV_duration", required=False,
    widget=forms.NumberInput(
    attrs={'data-slider-min': '0',
    'data-slider-max': '10',
    'data-slider-step': '1',
    'data-slider-value': 5}))

    phase_V_duration = forms.CharField(label="phase_V_duration", required=False,
    widget=forms.NumberInput(
    attrs={'data-slider-min': '0',
    'data-slider-max': '10',
    'data-slider-step': '1',
    'data-slider-value': 5}))

    class Meta:
        model = Session
        fields = ('phase_I_duration', 'phase_II_duration', 'phase_III_duration', 'phase_IV_duration', 'phase_V_duration', )

    def save(self,commit = True):
        data = self.cleaned_data

        session = super(AddSession, self).save(commit = False)
        session.phase_I_duration = 1 # self.cleaned_data["phase_I_duration"]
        session.phase_II_duration = self.cleaned_data["phase_II_duration"]
        session.phase_III_duration = self.cleaned_data["phase_III_duration"]
        session.phase_IV_duration = self.cleaned_data["phase_IV_duration"]
        session.phase_V_duration = self.cleaned_data["phase_V_duration"]

        if commit:
            session.save()

        return session

class SaveSession(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('phase_I_duration', 'phase_II_duration', 'phase_III_duration', 'phase_IV_duration', 'phase_V_duration', )

    def save(self,commit = True):

        session = super(SaveSession, self).save(commit = False)

        print('SaveSession')

        if commit:
            session.save()

        return session
