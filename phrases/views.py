from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Phrase, Translation
from .serializers import PhraseSerializer, TranslationSerializer


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

