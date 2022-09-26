from .models import *
from rest_framework import generics, permissions, serializers






class RegisterBusinessInvestorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BusinessInvestor
        fields = "__all__"

class RegisterIndividualInvestorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = IndividualInvestor
        fields = "__all__"

class RegisterAffliateSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Affliates
        fields = "__all__"

class RegisterSponsorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Sponsor
        fields = "__all__"

    



