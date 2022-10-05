from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import *
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from os import environ
from .serializers import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string




class BusinessInvestorRegisterView(APIView):
    def post(self, request, format=None):
        try:
            
            emailaddress = request.data['emailaddress']
            checkemaildup = duplicateEmails(BusinessInvestor, emailaddress)
            if not checkemaildup:
                serializer = RegisterBusinessInvestorSerializer(data=request.data)
                if serializer.is_valid():
                    passwd = make_password(
                    request.data['password'], salt=None, hasher='default')
                    serializer.save(password=passwd)
                    responseData = {'message': 'registration successful',
                                    'status': True}
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            responseData = {
                "message": "emailaddress already exist", 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")
        except Exception as e:
            responseData = {'message': 'An error occur' +
                                       str(e), 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")

class SaveEarninsView(APIView):
    def post(self, request, format=None):
        try:
            print(request.data['date_of_sale'])
            serializer = DashboardSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    valid_datetime = datetime.strptime(request.data['date_of_sale'], '%Y-%m-%d')
                    serializer.save(date_of_sale= valid_datetime)
                    responseData = {'message': 'Earnings created successfully',
                                    'status': True}
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
                except ValueError:
                    responseData = {'message': 'Invalid date format',
                                    'status': False}
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            responseData = {'message': 'An error occur' +
                                       str(e), 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")


class AllAffliatesView(APIView):
    def get(self, request, format=None):       
        try:
            affliate_list = Affliates.objects.all()
            serializer = ListAffliatesSerializer(affliate_list, many = True) 
            responseData = {'data': serializer.data, 'status': True}
            return HttpResponse(json.dumps(responseData))
        
        except Exception as e:
            return Response(str({e}))

class AffliateDashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None): 
        pk = request.query_params["affliateID"]
        try:
            model = Dashboard.objects.filter(affliateID__id = pk).values("affliateID__id", "affliateID__address", "affliateID__phonenumber", "affliateID__fullname",
            "sale_earnings", "earning_duration", "sale_type", "date_of_sale")
            items_detail = []
            total_sum = 0
            item_detail = {}
            
            affliate_data = {}

            
            for items in model:
                date_of_sale = items["date_of_sale"]
                sale_earnings = float(items["sale_earnings"])
                earning_duration = items["earning_duration"]
                affliate_fullname = items["affliateID__fullname"]
                sale_type = items["sale_type"]
                total_sum = sale_earnings + total_sum
                item_detail = {"sales_earnings":sale_earnings, "earning_duration":earning_duration,
                "affliate_fullname":affliate_fullname, "sale_type": sale_type,
                "date_of_sale":date_of_sale}
                items_detail.append(item_detail)
            affliate_data["total_earnings"] = total_sum
            affliate_data["total_sales"] = len(items_detail)
            affliate_data["data"] = items_detail
            affliate_data["status"] = True
            responseData = affliate_data 
        except Exception as e:
            responseData = {'message': str(e), 'status': True}
        return HttpResponse(json.dumps(responseData, default=str), content_type="application/json")




class IndividualInvestorRegisterView(APIView):
    def post(self, request, format=None):
        try:
        
            emailaddress = request.data['emailaddress']
            checkemaildup = duplicateEmails(IndividualInvestor, emailaddress)
            if not checkemaildup:
                serializer = RegisterIndividualInvestorSerializer(data=request.data)
                if serializer.is_valid():
                    passwd = make_password(
                    request.data['password'], salt=None, hasher='default')
                    serializer.save(password=passwd)
                    responseData = {'message': 'registration successful',
                                    'status': True}
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            responseData = {
                "message": "emailaddress already exist", 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")
        except Exception as e:
            responseData = {'message': 'An error occur' +
                                       str(e), 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")

class AffliateRegisterView(APIView):
    def post(self, request, format=None):
        try:
        
            emailaddress = request.data['emailaddress']
            checkemaildup = duplicateEmails(Affliates, emailaddress)
            if not checkemaildup:
                serializer = RegisterAffliateSerializer(data=request.data)
                if serializer.is_valid():
                    passwd = make_password(
                    request.data['password'], salt=None, hasher='default')
                    serializer.save(password=passwd)
                    responseData = {'message': 'registration successful',
                                    'status': True}
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            responseData = {
                "message": "emailaddress already exist", 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")
        except Exception as e:
            responseData = {'message': 'An error occur' +
                                       str(e), 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")

class SponsorRegisterView(APIView):
    def post(self, request, format=None):
        try:
            
            emailaddress = request.data['emailaddress']
            checkemaildup = duplicateEmails(Sponsor, emailaddress)
            if not checkemaildup:
                serializer = RegisterSponsorSerializer(data=request.data)
                if serializer.is_valid():
                    passwd = make_password(
                    request.data['password'], salt=None, hasher='default')
                    serializer.save(password=passwd)
                    responseData = {'message': 'registration successful',
                                    'status': True}
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            responseData = {
                "message": "emailaddress already exist", 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")
        except Exception as e:
            responseData = {'message': 'An error occur' +
                                       str(e), 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")


#Indivdual invester login api
class IndividualLoginView(APIView):
    def getToken(self):
        token = tokenGenerator()
        return token
    def post(self, request, format=None):
        try:
            token = self.getToken()
            access = token['access']
            refresh = token['refresh']
            emailaddress = request.data['username']
            password = request.data['password']
            record = IndividualInvestor.objects.filter(emailaddress=emailaddress).values("id",
            'emailaddress', 'firstname', 'lastname', 'about_us').first()
            
                
            if record:
                passwordvalue = list(IndividualInvestor.objects.filter(
                    emailaddress= emailaddress).values_list('password', flat=True))
                if passwordvalue:    
                    b = passwordvalue[0]
                    passwordconfirm = check_password(password, b)
                    if passwordconfirm:
                        return JsonResponse({'data': record, 'token': access, 'status': True})
                    return JsonResponse({'status': False, 'message': 'Invalid password'})
                return JsonResponse({'status': False, 'message': 'Invalid username'})
            return JsonResponse({'status': False, 'message': 'Invalid user'})
            
            
        except Exception as e:
            return JsonResponse({'message': e, 'status': False})


#Business invester login api
class BusinessInvestorLoginView(APIView):
    def getToken(self):
        token = tokenGenerator()
        return token
    def post(self, request, format=None):
        try:
            token = self.getToken()
            access = token['access']
            refresh = token['refresh']
            emailaddress = request.data['username']
            password = request.data['password']
            record = BusinessInvestor.objects.filter(emailaddress=emailaddress).values("id",
            'emailaddress', 'firstname', 'lastname', 'companyname', 'country', 'phonenumber').first()
            
                
            if record:
                passwordvalue = list(BusinessInvestor.objects.filter(
                    emailaddress= emailaddress).values_list('password', flat=True))
                if passwordvalue:    
                    b = passwordvalue[0]
                    passwordconfirm = check_password(password, b)
                    if passwordconfirm:
                        return JsonResponse({'data': record, 'token': access, 'status': True})
                    return JsonResponse({'status': False, 'message': 'Invalid password'})
                return JsonResponse({'status': False, 'message': 'Invalid username'})
            return JsonResponse({'status': False, 'message': 'Invalid user'})
            
            
        except Exception as e:
            return JsonResponse({'message': e, 'status': False})


#Affliate invester login api
class AffliateLoginView(APIView):
    def getToken(self):
        token = tokenGenerator()
        return token
    def post(self, request, format=None):
        try:
            token = self.getToken()
            access = token['access']
            refresh = token['refresh']
            emailaddress = request.data['username']
            password = request.data['password']
            record = Affliates.objects.filter(emailaddress=emailaddress).values("id",
            'emailaddress', 'fullname', 'address', 'fullname_kin', 'phonenumber','phonenumber_kin').first()
            
                
            if record:
                passwordvalue = list(Affliates.objects.filter(
                    emailaddress= emailaddress).values_list('password', flat=True))
                if passwordvalue:    
                    b = passwordvalue[0]
                    passwordconfirm = check_password(password, b)
                    if passwordconfirm:
                        return JsonResponse({'data': record, 'token': access, 'status': True})
                    return JsonResponse({'status': False, 'message': 'Invalid password'})
                return JsonResponse({'status': False, 'message': 'Invalid username'})
            return JsonResponse({'status': False, 'message': 'Invalid user'})
            
            
        except Exception as e:
            return JsonResponse({'message': e, 'status': False})

#Sponsor invester login api
class SponsorLoginView(APIView):
    def getToken(self):
        token = tokenGenerator()
        return token
    def post(self, request, format=None):
        try:
            token = self.getToken()
            access = token['access']
            refresh = token['refresh']
            emailaddress = request.data['username']
            password = request.data['password']
            record = Sponsor.objects.filter(emailaddress=emailaddress).values("id"
            'emailaddress', 'fullname', 'address', 'fullname_kin', 'phonenumber','phonenumber_kin').first()
            
                
            if record:
                passwordvalue = list(Sponsor.objects.filter(
                    emailaddress= emailaddress).values_list('password', flat=True))
                if passwordvalue:    
                    b = passwordvalue[0]
                    passwordconfirm = check_password(password, b)
                    if passwordconfirm:
                        return JsonResponse({'data': record, 'token': access, 'status': True})
                    return JsonResponse({'status': False, 'message': 'Invalid password'})
                return JsonResponse({'status': False, 'message': 'Invalid username'})
            return JsonResponse({'status': False, 'message': 'Invalid user'})
            
            
        except Exception as e:
            return JsonResponse({'message': e, 'status': False})


class RecoverAffliatePassword(APIView):
    def post(self, request, format=None):
        emailaddress = request.data['emailaddress']
        try:
            checkemail=Affliates.objects.get(emailaddress=emailaddress)
            checkemail = checkemail.emailaddress
        except Affliates.DoesNotExist:  # Be explicit about exceptions
            checkemail = None
        
        if checkemail:
           AffliatepasswordRecoveryEmail(emailaddress, request)
           responseData = {'message': 'Please check your email', 'status': True}
        else:
            responseData = {'message': 'Email address not found', 'status': False}
        return HttpResponse(json.dumps(responseData), content_type="application/json")

class RecoverIndivividualInvestorPassword(APIView):
    def post(self, request, format=None):
        emailaddress = request.data['emailaddress']
        try:
            checkemail=IndividualInvestor.objects.get(emailaddress=emailaddress)
            checkemail = checkemail.emailaddress
        except IndividualInvestor.DoesNotExist:  # Be explicit about exceptions
            checkemail = None
        
        if checkemail:
           passwordRecoveryEmail(emailaddress, request)
           responseData = {'message': 'Please check your email', 'status': True}
        else:
            responseData = {'message': 'Email address not found', 'status': False}
        return HttpResponse(json.dumps(responseData), content_type="application/json")

class RecoverBusinessInvestorPassword(APIView):
    def post(self, request, format=None):
        emailaddress = request.data['emailaddress']
        try:
            checkemail= BusinessInvestor.objects.get(emailaddress=emailaddress)
            checkemail = checkemail.emailaddress
        except BusinessInvestor.DoesNotExist:  # Be explicit about exceptions
            checkemail = None
        
        if checkemail:
           passwordRecoveryEmail(emailaddress, request)
           responseData = {'message': 'Please check your email', 'status': True}
        else:
            responseData = {'message': 'Email address not found', 'status': False}
        return HttpResponse(json.dumps(responseData), content_type="application/json")

class RecoverSponsorPassword(APIView):
    def post(self, request, format=None):
        emailaddress = request.data['emailaddress']
        try:
            checkemail=Sponsor.objects.get(emailaddress=emailaddress)
            checkemail = checkemail.emailaddress
        except Sponsor.DoesNotExist:  # Be explicit about exceptions
            checkemail = None
        
        if checkemail:
           passwordRecoveryEmail(emailaddress, request)
           responseData = {'message': 'Please check your email', 'status': True}
        else:
            responseData = {'message': 'Email address not found', 'status': False}
        return HttpResponse(json.dumps(responseData), content_type="application/json")


class PasswordRecovery(APIView):
    def post(self, request, format=None):
        userid = request.data['userid']
        uid = force_str(urlsafe_base64_decode(userid))
        try:
            affliate = Affliates.objects.get(emailaddress=uid)
            if affliate:
                print('working')
                password = make_password(
                    request.data['password'], salt=None, hasher='default')
                affliate.password = password
                affliate.save(update_fields = ["password"])
                responseData = {
                'message': 'Password has been changed',
                'status': True}
                return HttpResponse(json.dumps(responseData), content_type="application/json")
        except Affliates.DoesNotExist:
            user = None
            responseData = {
                'message': 'The record cannot be found',
                'status': False
            }
            return HttpResponse(json.dumps(responseData), content_type="application/json")
        
        try:
            sponsor = Sponsor.objects.get(emailaddress = uid)
            if sponsor:
                sponsor = Sponsor.objects.get(emailaddress=uid)
                password = make_password(
                    request.data['password'], salt=None, hasher='default')
                sponsor.password = password
                sponsor.save(update_fileds = "password")
                responseData = {
                'message': 'Password changed',
                'status': True}
                return HttpResponse(json.dumps(responseData), content_type="application/json")
            
        except Sponsor.DoesNotExist:
            sponsor = None
            responseData = {
                'message': 'The record cannot be found',
                'status': False
            }
            return HttpResponse(json.dumps(responseData), content_type="application/json")

        try:
            business_investor = BusinessInvestor.objects.get(emailaddress = uid)
            if business_investor:
        
                password = make_password(
                    request.data['password'], salt=None, hasher='default')
                business_investor.password = password
                business_investor.save(update_fields = ["password"])
                responseData = {
                'message': 'Password has been changed',
                'status': True
                }
                return HttpResponse(json.dumps(responseData), content_type="application/json")
        except BusinessInvestor.DoesNotExist:
            business_investor = None
            responseData = {
                'message': 'The record cannot be found',
                'status': False
            }
            return HttpResponse(json.dumps(responseData), content_type="application/json")

class PitchProjectView(APIView):
    
    def post(self, request, format=None):
        try:
            email = request.data["emailaddress"]
            
            serializer = PitchSerializer(data=request.data)
            if serializer.is_valid():
                
                serializer.save()
                
                EmailPitch(email)
                responseData = {'message': 'Pitch created successfully',
                                'status': True}
                return HttpResponse(json.dumps(responseData), content_type="application/json")
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            responseData = {'message': 'An error occurred' +
                                       str(e), 'status': False}
            return HttpResponse(json.dumps(responseData), content_type="application/json")



            

#this function helps us generate access and refresh tokens
def tokenGenerator():
    username = environ.get('USERNAME_TOKEN')
    password = environ.get('PASSWORD_TOKEN')
    headers = {'content-type': "application/json"}
    params = {"username": username, "password": password}
    url = settings.APP_URL
    fullurl = f"{url}/api/token/"
    r = requests.post(fullurl, data=params, verify=False)
    record = r.json()
    return record

def duplicateEmails(model,useremailaddress):
    email = model.objects.filter(emailaddress=useremailaddress)
    if not email:
        return False
    else:
        return True

def AffliatepasswordRecoveryEmail(emailaddress, request):
    subject = 'Password Recovery'
    template_name = 'password_recovery.html'
    from_email = settings.DEFAULT_FROM_EMAIL
    kwargs = {"uidb64": urlsafe_base64_encode(
        force_bytes(emailaddress))}
    text_content = {}
    host = settings.APP_URL
    activate_url = "{0}://{1}/{2}{3}".format(
        request.scheme, host, 'affliate_reset.html?token=', urlsafe_base64_encode(force_bytes(emailaddress)))
    context = {'activate_url': activate_url}
    html_content = render_to_string(template_name, context)
    email = EmailMultiAlternatives(
        subject, text_content, from_email, [emailaddress])
    email.attach_alternative(html_content, "text/html")
    email.send()

def passwordRecoveryEmail(emailaddress, request):
    subject = 'Password Recovery'
    template_name = 'password_recovery.html'
    from_email = settings.DEFAULT_FROM_EMAIL
    kwargs = {"uidb64": urlsafe_base64_encode(
        force_bytes(emailaddress))}
    text_content = {}
    host = settings.APP_URL
    activate_url = "{0}://{1}/{2}{3}".format(
        request.scheme, host, 'forgot-password/reset/?token=', urlsafe_base64_encode(force_bytes(emailaddress)))
    context = {'activate_url': activate_url}
    html_content = render_to_string(template_name, context)
    email = EmailMultiAlternatives(
        subject, text_content, from_email, [emailaddress])
    email.attach_alternative(html_content, "text/html")
    email.send()

def EmailPitch(emailaddress):
    subject = 'Project Pitch'
    template_name = 'projectpitch.html'
    from_email = settings.DEFAULT_FROM_EMAIL
    pitcher=Pitch.objects.filter(emailaddress=emailaddress).values("id",'firstname','lastname','emailaddress',
    "phonenumber","city", "load_capacity", "extra_details", "no_of_users").first()
    recipientemail ="chidera.adimegwu@sparknigeria.co"
    
    from_email = "{0}".format(settings.DEFAULT_FROM_EMAIL)
    fullname= "{0}{1}{2}".format(pitcher['lastname'],' ',pitcher['firstname'])
    emailaddress = f"{pitcher['emailaddress']}"
    phonenumber = f"{pitcher['phonenumber']}"
    city = f"{pitcher['city']}"
    load_capacity = f"{pitcher['load_capacity']}"
    extra_details = f"{pitcher['extra_details']}"
    no_of_users = f"{pitcher['no_of_users']}"

    context = {'fullname':fullname,'subject':subject, 'emailaddress':emailaddress,
    'phonenumber':phonenumber, 'city':city, 'load_capacity':load_capacity, 'extra_details':extra_details,'no_of_users':no_of_users}
    text_content = {}
    html_content = render_to_string(template_name, context)
    #print('Html content {}'.format(html_content))
    email = EmailMultiAlternatives(subject,text_content, from_email,[recipientemail])
    email.attach_alternative(html_content, "text/html")
    email.send()
    return None
    






