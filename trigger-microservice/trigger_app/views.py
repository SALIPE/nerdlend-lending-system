
import json

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .email_utils import enviar_email
from .models import Trigger
from .serializers import TriggerSerializer


class TriggerEmailView(APIView):
    def post(self, request):
        payload = request.data

        # Validate payload
        required_fields = ["email", "subject", "message", "scheduleid"]
        missing_fields = [field for field in required_fields if field not in payload]
        if missing_fields:
            return Response(
                {"error": f"Missing fields: {', '.join(missing_fields)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        log = TriggerSerializer(data={
                                        "ccmessage":json.dumps({
                                            "destinatario":payload.get("email"), 
                                            "assunto":payload.get("subject"), 
                                            "mensagem":payload.get("message")
                                        }),
                                        "cvscheduleid":payload.get("scheduleid")
                                    })
        if log.is_valid():
            log.save()
        else:
            print(log.errors)
        try:
            enviar_email(
                destinatario=payload.get("email"), 
                assunto=payload.get("subject"), 
                mensagem=payload.get("message")
            )
            return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)