from rest_framework import serializers
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'updated_at', 'sensor', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']