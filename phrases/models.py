from django.db import models
from django.urls import reverse
import pycountry
from datamuse import datamuse
from translate import Translator

datamuseAPI = datamuse.Datamuse()


class Languages(models.Model):
    LANGUAGES = sorted([(lang.alpha_3, lang.name) for lang in pycountry.languages], key=lambda l: l[1])
    DEFAULT_LANGUAGE = (pycountry.languages.get(alpha_3="eng").alpha_3,
                        pycountry.languages.get(alpha_3="eng").name)

    language = models.CharField(max_length=3,
                                choices=LANGUAGES,
                                default=DEFAULT_LANGUAGE[0])


class Translation(Languages, models.Model):
    content = models.TextField()

    class Meta:
        indexes = [models.Index(fields=["content"])]
        ordering = ["content"]
        verbose_name = "translation"
        verbose_name_plural = "translations"

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("translation_detail", args=[str(self.id)])


class Phrase(Languages, models.Model):
    SIMILAR_COUNT = 3

    translator = Translator(to_lang="uk")  # TODO: use value from user.default_to_lang

    text = models.CharField(max_length=100)
    translations = models.ManyToManyField(Translation)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["text"])]
        ordering = ["text"]
        verbose_name = "phrase"
        verbose_name_plural = "phrases"

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("phrase_detail", args=[str(self.id)])

    @property
    def similar(self):
        similar_words = datamuseAPI.words(ml=self.text, max=self.SIMILAR_COUNT)

        return similar_words

    @property
    def auto_translation(self):
        return self.translator.translate(self.text)


class Mention(models.Model):
    content = models.TextField()
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE, null=True, related_name="mentions")

    class Meta:
        indexes = [models.Index(fields=["content"])]
        ordering = ["content"]
        verbose_name = "mention"
        verbose_name_plural = "mentions"

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("mention_detail", args=[str(self.id)])
