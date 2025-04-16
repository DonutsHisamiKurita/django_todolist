from django.forms import ModelForm
from .models import ToDoItem

class ToDoForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('title','description')