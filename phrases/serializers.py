from rest_framework import serializers

from .models import Phrase, Translation, Mention


class TranslationSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=Translation.LANGUAGES, required=True)

    class Meta:
        model = Translation
        fields = ("id", "content", "language")

    def create(self, validated_data):
        phrase_pk = validated_data.pop("phrase")
        translation = Translation.objects.create(**validated_data)
        phrase = Phrase.objects.get(pk=phrase_pk)

        phrase.translations.add(translation)

        return translation


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ("id", "content", "phrase")


class PhraseSerializer(serializers.ModelSerializer):
    translations = serializers.StringRelatedField(many=True, read_only=True)
    similar = serializers.SerializerMethodField()
    mentions = MentionSerializer(many=True, read_only=True)

    class Meta:
        model = Phrase
        fields = ("id", "text", "translations", "created_at", "updated_at", "similar", "auto_translation", "mentions")

    def get_similar(self, obj):
        return [item.get("word") for item in obj.similar]
