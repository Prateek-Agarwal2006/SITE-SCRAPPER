from rest_framework import serializers

class GPUDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.CharField(max_length=50)