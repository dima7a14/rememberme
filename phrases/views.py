from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Phrase, Translation, Mention
from .serializers import PhraseSerializer, TranslationSerializer, MentionSerializer


class PhraseViewSet(viewsets.ModelViewSet):
    """
    A viewset for phrases.
    """
    serializer_class = PhraseSerializer
    permission_classes = []
    queryset = Phrase.objects.all()

    @action(detail=True, methods=["patch", "delete"])
    def translation(self, request, pk=None):
        phrase = self.get_object()

        serializer = TranslationSerializer(data=request.data)

        if serializer.is_valid():
            translation = Translation.objects.create(**serializer.validated_data)
            phrase.translations.add(translation)
            phrase.save()
            return Response({"status": True}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranslationViewSet(viewsets.ModelViewSet):
    """
    A viewset for translations.
    """
    serializer_class = TranslationSerializer
    permission_classes = []

    def get_queryset(self):
        return Translation.objects.filter(phrase=self.kwargs["phrase_pk"])

    def perform_create(self, serializer):
        serializer.save(phrase=self.kwargs["phrase_pk"])


class MentionViewSet(viewsets.ModelViewSet):
    """
    A viewset for mentions.
    """
    serializer_class = MentionSerializer
    permission_classes = []

    def get_queryset(self):
        return Mention.objects.filter(phrase=self.kwargs["phrase_pk"])

    def perform_create(self, serializer):
        phrase = Phrase.objects.get(pk=self.kwargs["phrase_pk"])
        serializer.save(phrase=phrase)
