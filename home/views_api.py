from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'
        try:
            data = request.data

            if data.get('username') is None or data.get('username') == '':
                response['message'] = 'Please enter Username'
                raise Exception('User not found')
            
            if data.get('password') is None or data.get('password') == '':
                response['message'] = 'Please enter Password'
                raise Exception('Password not found')

            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'Invalid Username. User not found.'
                raise Exception('Incorrect Username')

            user_obj = authenticate(username = data.get('username') , password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome!'
            else:
                response['message'] = 'Incorrect password.'
                raise Exception('Incorrect password')

        except Exception as e:
            print(e)

        return Response(response)

LoginView = LoginView.as_view()


class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'
        try:
            data = request.data

            if data.get('username') is None or data.get('username') == '':
                response['message'] = 'Please enter Username'
                raise Exception('key username not found')
            
            if data.get('email') is None or data.get('email') == '':
                response['message'] = 'Please enter Email'
                raise Exception('key email not found')
            
            if data.get('password') is None or data.get('password') == '':
                response['message'] = 'Please enter Password'
                raise Exception('key password not found')

            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username taken')

            check_user = User.objects.filter(email = data.get('email')).first()

            if check_user:
                response['message'] = 'Email already registered'
                raise Exception('Email register')

            user_obj = User.objects.create_user(username = data.get('username'), email = data.get('email'), password = data.get('password'))
            user_obj.save
            response['message'] = 'User created!'
            response['status'] = 200

        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()


# "username" : "Public", "password" : "123"