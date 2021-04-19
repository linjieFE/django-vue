form rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer)
    class Meta:
        model = Blog