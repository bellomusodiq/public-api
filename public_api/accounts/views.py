from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from api_requests.authentication import auth
from .models import ApiToken, User, Investor, Transaction
from rest_framework.permissions import IsAuthenticated
from api_requests.update_investor import update_investor
from api_requests.create_investor import create_investor
from api_requests.get_market_symbol import get_market_symbol
from api_requests.get_market_data import get_market_data
from api_requests.get_investors import get_investors
from api_requests.create_transaction import create_transaction
from api_requests.get_transactions import get_transactions
from api_requests.update_kyc import update_kyc
from api_requests.cancel_transaction import cancel_transaction
from .serializers import TransactionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your views here.


def home(request):

    return HttpResponse('<h1>Hello world</h1>')


def convert_date(date):
    [year, month, day] = date.split('-')
    return month + '-' + day + '-' + year


def field_verification(data: dict, fields: list):
    errors = {}
    for field in fields:
        if not data.get(field):
            errors[field] = '{} field cannot be blank'.format(field)
    return errors


class GetAccessToken(APIView):

    def post(self, request):
        response = auth()
        print(response)
        if response['status'] != 201:
            return Response({'message': 'invalid access login details'}, 400)
        api_token = ApiToken.objects.first()
        if api_token:
            api_token.access_token = response['data']['access_token']
            api_token.referesh_token = response['data']['refresh_token']
            api_token.token_type = response['data']['token_type']
            api_token.expires_in = response['data']['expires_in']
            api_token.save()
        else:
            ApiToken.objects.create(
                access_token = response['data']['access_token'],
                referesh_token = response['data']['refresh_token'],
                token_type = response['data']['token_type'],
                expires_in = response['data']['expires_in'],
            )
        return Response({'message': 'api login successful'})


class CreateCustomer(APIView):

    def post(self, request):
        errors = field_verification(request.data, [
            'title',
            'surname',
            'first_name',
            'other_names',
            'gender',
            'phone',
            'date_of_birth',
            'email_address',
            'home_phone',
            'address',
            'country',
            'state',
            'nationality',
            'state_of_origin',
            'city',
            'lga',
            'bank_account_number',
            'bank_account_name',
            'bank_name',
            'bank_code',
            'bvn',
            'company_name',
            'employment_type',
            'occupation',
            'identity_type',
            'identity_number',
            'expiry_date',
            'politically_exposed',
            'next_of_kin_name',
            'next_of_kin_address',
            'next_of_kin_email',
            'next_of_kin_phone_number',
            'next_of_kin_relationship',
            'password'
        ])
        if User.objects.filter(username=request.data.get('email_address')).first():
            errors['email'] = 'this email has been registered'
        if len(errors) > 0:
            return Response({'errors': errors}, 400)
        
        api_token = ApiToken.objects.first()
        gender = request.data['gender']
        if gender == 'Male':
            gender = 'M'
        else:
            gender = 'F'
        if not api_token:
            return Response({'message': 'api authentication is required'}, 403)
        response = create_investor(
            api_token.access_token, request.data['title'], request.data['surname'], request.data['first_name'],
            request.data['other_names'], gender, request.data['phone'],
            convert_date(request.data['date_of_birth']), request.data['email_address'], request.data['home_phone'],
            request.data['address'], request.data['country'], request.data['state'],
            request.data['nationality'], request.data['state_of_origin'], request.data['city'],
            request.data['lga'], request.data['bank_account_number'], request.data['bank_name'],
            request.data['bank_account_name'],
            request.data['bank_code'], request.data['bvn'], request.data['company_name'],
            request.data['employment_type'], request.data['occupation'], request.data['identity_type'],
            request.data['identity_number'], convert_date(request.data['expiry_date']), request.data['politically_exposed'],
            request.data['next_of_kin_name'], request.data['next_of_kin_address'], request.data['next_of_kin_email'], 
            request.data['next_of_kin_phone_number'],
            request.data['next_of_kin_relationship']
        )
        print(response)
        if response['status'] == 400:
            return Response({'errors': response['errors']}, 400)
        if response['status'] == 201:
            user = User.objects.create(
                username=request.data['email_address'],
                email=request.data['email_address']
            )
            user.set_password(request.data['password'])
            user.save()
            Investor.objects.create(
                user=user,
                investor_id=response['data']['investor_id'],
                investor_no=response['data']['investor_no'],
            )
            return Response({'data': response['data']}, 201)
        return Response({'message': 'something went wrong'}, 400)


class UpdateCustomer(APIView):

    def post(self, request):
        errors = field_verification(request.data, [
            'id',
            'title',
            'surname',
            'first_name',
            'other_names',
            'gender',
            'phone',
            'date_of_birth',
            'email_address',
            'address',
            'country',
            'state',
            'nationality',
            'city',
            'bank_account_number',
            'bank_account_name',
            'bank_name',
            'bank_code',
            'branch_code',
            'acc_type',
            'company_name',
            'next_of_kin_name',
        ])
        user = User.objects.filter(username=request.data.get('email_address')).first()
        if user:
            if user != request.user:
                errors['email'] = 'this email has been registered'
        if len(errors) > 0:
            return Response({'errors': errors}, 400)
        
        api_token = ApiToken.objects.first()
        if not api_token:
            return Response({'message': 'api authentication is required'}, 403)
        response = update_investor(
            api_token.access_token, request.data['id'], request.data['title'], 
            request.data['surname'], request.data['first_name'], request.data['other_names'], 
            request.data['gender'], request.data['phone'], request.data['date_of_birth'], 
            request.data['email_address'], request.data['address'], request.data['country'], 
            request.data['state'], request.data['nationality'], request.data['city'],
            request.data['bank_account_number'], request.data['bank_account_name'],
            request.data['bank_code'], request.data['branch_code'], request.data['acc_type'],
            request.data['company_name'], request.data['next_of_kin_name']
        )
        print(response)
        if response['status'] == 400:
            return Response({'errors': response['errors']}, 400)
        if response['status'] == 200:
            user = request.user
            user.username=request.data['email_address']
            user.email=request.data['email_address']
            user.save()
            return Response({'data': response['data']}, 200)
        return Response({'message': 'something went wrong'}, 400)


class GetMarketSymbol(APIView):

    def get(self, request):
        category = request.GET.get('category')
        response = None
        access_token = ApiToken.objects.first().access_token
        if not category:
            response = get_market_symbol(access_token)
        else:
            response = get_market_symbol(access_token, category=category)
        if response['status'] == 200:
            return Response({'data': response['data']})
        return Response({'error': 'something went wrong'}, 400)


class GetMarketData(APIView):

    def get(self, request):
        category = request.GET.get('category')
        response = None
        access_token = ApiToken.objects.first().access_token
        if not category:
            response = get_market_data(access_token)
        else:
            response = get_market_data(access_token, category=category)
        if response['status'] == 200:
            return Response({'data': response['data']})
        return Response({'error': 'something went wrong'}, 400)


class GetInvestors(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):

        access_token = ApiToken.objects.first().access_token
        response = get_investors(access_token)
        print(response)
        if response['status'] == 200:
            return Response({'data': response['data']})
        return Response({'error': 'something went wrong'}, 400)


class GetInvestorById(APIView):

    def get(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            access_token = ApiToken.objects.first().access_token
            response = get_investors(access_token, id_=user.investor.investor_id)
            print(response)
            if response['status'] == 200:
                return Response({'data': response['data']})
            return Response({'error': 'something went wrong'}, 400)
        except Exception as error:
            print(error)
            return Response({'error': 'user with this id does not exist'}, 404)


class CreateListTransaction(APIView):

    permission_classes = [IsAuthenticated]

    access_token = ApiToken.objects.first().access_token

    def post(self, request):

        errors = field_verification(request.data, [
            'instructions',
            'trade_date_limit', 
            'trade_effective_date',
            'trade_action',
            'trade_price_limit',
            'trade_units',
            'stock_code'
        ])
        if len(errors) > 0:
            return Response({'errors': errors}, 400)
        try:
            user = request.user
            response = create_transaction(self.access_token, user.investor.investor_id, request.data['instructions'],
            convert_date(request.data['trade_date_limit']), request.data['trade_action'], request.data['trade_price_limit'], convert_date(request.data['trade_effective_date']),
            request.data['trade_units'], request.data['stock_code'])
            print(response)
            if response['status'] == 200:
                Transaction.objects.create(
                    user=user,
                    transaction_ref=response["transaction_ref"],
                    instructions=request.data['instructions'],
                    trade_date_limit=convert_date(request.data['trade_date_limit']),
                    trade_effective_date=convert_date(request.data['trade_effective_date']),
                    trade_action=request.data['trade_action'],
                    trade_price_limit=request.data['trade_price_limit'],
                    trade_unit=request.data['trade_units'],
                    stock_code=request.data['stock_code'],
                )
                print(response['transaction_ref'])
                return Response({'message': 'transaction has been created successfully'})
            return Response({'error': 'something went wrong'}, 400)
        except Exception as error:
            print(error)
            return Response({'error': 'user does not exist'}, 404)

    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        response = get_transactions(self.access_token, start_date=start_date, end_date=end_date)
        print(response)
        if response['status'] == 200:
            return Response({'data': response['data']})
        return Response({'error': 'bad request'}, 400)


class UpdateKyc(APIView):

    def post(self, request):

        errors = field_verification(request.data, ['files'])

        if len(errors) > 0:
            return Response(errors, 400)

        access_token = ApiToken.objects.first().access_token
        response = update_kyc(access_token, request.data['id'], 
        request.data.get('files').file)

        print(response)
        if response['status'] == 200:
            return Response({'data': response['data']})
        return Response({'error': 'something went wrong'}, 400)


class CancelTransaction(APIView):

    def delete(self, delete, pk=None):
        try:
            transaction = Transaction.objects.get(pk=pk)
            access_token = ApiToken.objects.first().access_token
            response = cancel_transaction(access_token, transaction.transaction_ref)
            print(response)
        except Transaction.DoesNotExist:
            return Response({'error': 'transaction cannot be found'}, 404)


class TransactionViewSet(ModelViewSet):

    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()

        user = self.request.GET.get('user')
        if user:
            queryset = queryset.filter(user=user)

        return queryset



def jwt_response_payload_handler(token, user=None, request=None):
    return dict(token=token, userid=user.id)
