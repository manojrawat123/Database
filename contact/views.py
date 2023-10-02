from contact.serializers import ContactSerializer
from contact.models import Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail

class ContactViewSet(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            email_from = settings.EMAIL_HOST_USER
            email = "positive.mind.123456789@gmail.com"
            recipient_list = [email,]
            subject = "Lead Add Sucessfully" 
            
            data = serializer.save()
            lead_name = serializer.data.get('LeadName', 'Student')
            message = f''''
            Dear Manoj Rawat there is some activity in your hosted website.
            {serializer.data}
            '''
            send_mail(subject, message, email_from, recipient_list)
            return Response({"msg": "Registration Sucessfully"})
        return Response({"error": "Invalid Data" }, status=status.HTTP_400_BAD_REQUEST)
           