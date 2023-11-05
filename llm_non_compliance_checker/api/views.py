
from rest_framework.views import APIView
from rest_framework.response import Response
from api.utills.exceptions import CustomAPIException
from api.serializers import ComplianceCheckSerializer
from api.compliance_checker.compliance_checker import ComplianceChecker


class ComplianceCheck(APIView):
    def get(self, request, *args, **kwargs):

        # validating fields with serializers automatic field validation
        serializer = ComplianceCheckSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        webpage_url = serializer.validated_data['webpage_url']
        compliance_policy_url = serializer.validated_data['compliance_policy_url']
        compliance_checker = ComplianceChecker(policy_url=compliance_policy_url, web_page_url=webpage_url)
        non_compliance_response = compliance_checker.find_non_compliance_results()


        return Response(non_compliance_response)