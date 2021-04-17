from django.contrib import admin
from django.urls import reverse, reverse_lazy
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Phrase, Translation, Mention


def render_link(url: str, content: str) -> str:
    return f"<a target=\"_blank\" href=\"{url}\">{content}<a/>"


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("text", "concat_translations", "created_at")
    search_fields = ("text", "translations__content")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("created_at", "text")
    fields = ("text", "language", "translations")

    def concat_translations(self, obj):
        translations = []

        for translation in obj.translations.all():
            url = reverse("admin:phrases_translation_change", args=(translation.id,))
            translations.append(render_link(url, translation.content))


        return format_html("; ".join(translations))

    concat_translations.short_description = "Translations"


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("content", "connected_phrases", "language")
    search_fields = ("content", "phrase_set__text")
    ordering = ("content",)
    fields = ("content", "language")

    def connected_phrases(self, obj):
        phrases = []

        for phrase in obj.phrase_set.all():
            url = reverse("admin:phrases_phrase_change", args=(phrase.id,))
            phrases.append(render_link(url, phrase.text))


        return format_html("; ".join(phrases))

    connected_phrases.short_description = "Used in phrases"


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ("content", "origin_phrase")
    search_fields = ("content", "phrase__text")
    ordering = ("content",)

    def origin_phrase(self, obj):
        url = reverse("admin:phrases_phrase_change", args=(obj.phrase.id,))

        return format_html(render_link(url, obj.phrase.text))

    origin_phrase.short_description = "Phrase"
