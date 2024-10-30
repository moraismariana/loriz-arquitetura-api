import os
from django.db import models
from rest_framework import serializers

class DeleteOldImageMixin:
    """Mixin para deletar imagens antigas ao atualizar ou deletar o objeto."""

    def _delete_old_file(self, old_file, new_file):
        """Deleta o arquivo antigo se ele for diferente do novo."""
        if old_file and old_file != new_file and os.path.isfile(old_file.path):
            old_file.delete(save=False)

    def save(self, *args, **kwargs):
        if self.pk:  # Se o objeto já existe no banco de dados
            old_instance = self.__class__.objects.get(pk=self.pk)
            # Deleta as imagens antigas para todos os campos de imagem do modelo
            for field in self._get_image_fields():
                old_file = getattr(old_instance, field)
                new_file = getattr(self, field)
                self._delete_old_file(old_file, new_file)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Deleta todas as imagens associadas ao objeto."""
        for field in self._get_image_fields():
            file = getattr(self, field)
            if file and os.path.isfile(file.path):
                file.delete(save=False)
        super().delete(*args, **kwargs)

    def _get_image_fields(self):
        """Retorna uma lista dos nomes dos campos de imagem do modelo."""
        return [
            field.name for field in self._meta.fields
            if isinstance(field, models.ImageField)
        ]


class DeleteOldImageSerializerMixin:
    """Mixin para deletar imagens antigas ao atualizar o objeto via serializer."""

    def update(self, instance, validated_data):
        for field in self._get_image_fields(instance):
            nova_imagem = validated_data.get(field, None)
            if nova_imagem:
                imagem_antiga = getattr(instance, field)
                if imagem_antiga and imagem_antiga != nova_imagem:
                    imagem_antiga.delete(save=False)

        return super().update(instance, validated_data)

    def _get_image_fields(self, instance):
        """Retorna uma lista dos nomes dos campos de imagem do objeto."""
        return [
            field.name for field in instance._meta.fields
            if isinstance(field, serializers.ImageField)
        ]