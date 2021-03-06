from django import forms
from UmbrellaSocial.posts import models
from UmbrellaSocial.posts.models import Group


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('message', 'group')
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['group'].queryset = (
                Group.objects.filter(
                    pk__in=user.groups.values_list('group__pk')
                )
            )
