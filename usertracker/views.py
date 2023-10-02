from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
from usertracker.models import UserTracer
from usertracker.serilizers import UserTracerSerializer

class UserTracerView(APIView):
    def get(self, request):
        usertracer = UserTracer.objects.all()
        serializer = UserTracerSerializer(usertracer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserTracerSerializer(data=request.data)
        if serializer.is_valid():
            email_from = settings.EMAIL_HOST_USER
            email = "positive.mind.123456789@gmail.com"
            recipient_list = [email,]
            subject = "Lead Add Sucessfully"             
            data = serializer.save()
            message = f''''            
            Dear Manoj Rawat there is some activity in your hosted website.
            {serializer.data} 
            '''
            send_mail(subject, message, email_from, recipient_list)
            return Response({"msg": "Registration Sucessfully"})
        return Response({"error": "Invalid Data" }, status=status.HTTP_400_BAD_REQUEST)
           