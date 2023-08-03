from rest_framework import serializers
from .models import magang

class MagangSerializers(serializers.ModelSerializer):
    class Meta:
        model = magang
        fields = ["id", "Judul", "Jurusan", "Deskripsi", "Deadline", "Publish", "Nama_id", "is_closed", "file"]