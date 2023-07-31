from modeltranslation.translator import translator, TranslationOptions
from apps.api.todo.models import Todo


class TranslationTodo(TranslationOptions):
    fields = ('title', 'desc')


translator.register(Todo, TranslationTodo)
