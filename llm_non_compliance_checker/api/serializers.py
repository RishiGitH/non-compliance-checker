
from rest_framework import serializers

class ComplianceCheckSerializer(serializers.Serializer):
    webpage_url = serializers.URLField()
    compliance_policy_url = serializers.URLField()