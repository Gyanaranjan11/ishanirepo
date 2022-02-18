# from django.contrib import messages
# from django.db.models import Q
# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from user_auth.models import UserModel
# from django.contrib.auth.models import User
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth import login
# from user_auth.sms import sendSMS
# from django.core.mail import send_mail, EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from pgbooking import settings
# from datetime import date
# import pyotp
# import base64

def home(request):
    return render(request, "Home.html")


def privacy(request):
    return render(request, "privacy.html")


def term(request):
    return render(request, 'term.html')

#
#
# def profile(request):
# 	try:
# 		data = UserModel.objects.get(email=request.session["email"])
# 		context = {
# 		"data": data,
# 		"email":request.session["email"],
# 		}
# 		return render(request, 'user/profile.html', context)
# 	except:
# 		return render(request, 'user/profile.html')
#
#
# def edit_bd(request):
# 	try:
# 		data = UserModel.objects.get(email=request.session["email"])
# 		if request.method == "POST":
# 			f_name = request.POST["f_name"]
# 			l_name = request.POST["l_name"]
# 			dob = request.POST["dob"]
# 			optradio = request.POST["optradio"]
# 			UserModel.objects.filter(email=request.session["email"]).update(
# 				f_name=f_name,l_name=l_name,dob=dob,gender=optradio)
# 			return redirect('profile')
# 		context = {
# 		"data": data,
# 		"edit_bd": True,
# 		"email":request.session["email"],
# 		}
# 		return render(request, 'user/profile.html', context)
# 	except:
# 		return render(request, 'user/profile.html')
#
#
# def edit_ad(request, id):
# 	try:
# 		data = UserModel.objects.get(email=request.session["email"])
# 		if request.method == "POST":
# 			if data.email == request.POST['email']:
# 				email = request.POST['email']
# 				email_verify = data.email_verify
# 			elif data.email == "":
# 				email = data.email
# 				email_verify = data.email_verify
# 			else:
# 				email = request.POST['email']
# 				email_verify = "not_verified"
# 			if data.mob_no == request.POST['mob_no']:
# 				mob_no = request.POST['mob_no']
# 				mob_no_verify = data.mob_no_verify
# 			elif data.mob_no == "":
# 				mob_no = data.mob_no
# 				mob_no_verify = data.mob_no_verify
# 			else:
# 				mob_no = request.POST['mob_no']
# 				mob_no_verify = "not_verified"
# 			UserModel.objects.filter(email=request.session["email"]).update(
# 				mob_no=mob_no,mob_no_verify=mob_no_verify,
# 				email=email,email_verify=email_verify)
# 			return redirect('profile')
#
# 		context = {
# 		"data": data,
# 		"edit_ad": True,
# 		"email":request.session["email"],
# 		}
# 		print("here")
# 		return render(request, 'user/profile.html', context)
# 	except Exception as e:
# 		print(str(e))
# 		return render(request, 'user/profile.html')
#
#
# def edit_photo(request):
# 	try:
# 		data = UserModel.objects.get(email=request.session["email"])
# 		if request.method == 'POST':
# 			photo = request.FILES["photo"]
# 			UserModel(id=data.id, email=data.email,user=data.user,name=data.name,
# 				f_name=data.f_name,l_name=data.l_name,dob=data.dob,email_verify=data.email_verify,
# 				mob_no=data.mob_no,mob_no_verify=data.mob_no_verify,password=data.password,
# 				gender=data.gender,status=data.status,created_date=data.created_date,
# 				photo=photo,p_status="normal").save()
# 			return redirect('profile')
# 		context = {
# 		"data": data,
# 		"edit_photo": True,
# 		"email":request.session["email"],
# 		}
# 		return render(request, 'user/profile.html', context)
# 	except Exception as e:
# 		print(e)
# 		return render(request, 'user/profile.html')
#
#
# # def home(request):
# # 	try:
# # 		data = UserModel.objects.get(email=request.session["email"])
# # 		context = {
# # 		"data": data,
# # 		"email":request.session["email"],
# # 		}
# # 		return render(request, 'user/home.html', context)
# # 	except:
# # 		return render(request, 'user/home.html')
#
#
#
# def sociallogin(request):
# 	if not UserModel.objects.filter(user__username=request.user.username).exists():
# 		for i in User.objects.filter(username=request.user.username).values('socialaccount__extra_data'):
# 			picture = i["socialaccount__extra_data"]["picture"]
# 		auto_psd = User.objects.make_random_password(length=12,allowed_chars="@abcdefghjkmnpqrstuvwxyz0123456789@#")
# 		name = str(request.user.first_name + " "+ request.user.last_name)
# 		email=request.user.email
# 		UserModel(user=User.objects.get(username=request.user.username),
# 			email=request.user.email,photo=picture,p_status="s_photo",password=auto_psd,
# 			email_verify= "verified",name= str(request.user.first_name + " "+ request.user.last_name)
# 			,f_name=request.user.first_name,l_name=request.user.last_name).save()
#
# 		subject = "“You successfully created an account.”"
# 		message = f"Dear ({name}). Welcome to Booking PG. ({email}) is your email address and ({auto_psd}) is your password. Now you can visit our website and BOOK your PG."
# 		html_content = render_to_string("user/email_template.html", {'message': message})
# 		text_content = strip_tags(html_content)
# 		email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
# 		email.attach_alternative(html_content, "text/html")
# 		email.send()
# 		messages.success(request, "Your password is send to your Email-id successfully, do not share with anyone.")
# 	request.session["email"] = request.user.email
# 	return redirect('welcom')
#
#
# def login(request):
# 	if not request.user.is_authenticated:
# 		if request.method == 'POST':
# 			email = request.POST.get('u_email')
# 			password = request.POST.get('u_pass')
# 			if UserModel.objects.filter(Q(mob_no=email) | Q(email=email), password=password).exists():
# 				data = UserModel.objects.filter(Q(mob_no=email) | Q(email=email), password=password)
# 				for i in data:
# 					request.session["email"] = i.email
# 					request.session["id"] = i.id
# 					request.session["mob_no"] = i.mob_no
# 				messages.success(request, "Successfully login.")
# 				return redirect('welcom')
# 			else:
# 				messages.error(request, "User Does n't Exist")
# 				return render(request, 'user/login.html')
# 		if request.method == 'GET':
# 			if request.user.is_authenticated:
# 				return redirect('welcom')
# 			else:
# 				return render(request, "user/login.html")
# 	else:
# 		return redirect('welcom')
#
#
# def woner_login(request):
# 	return render(request, "user/woner_login.html")
#
#
# def signup(request):
# 	if request.method == 'POST':
# 		name = request.POST['name']
# 		email = request.POST['email']
# 		mobno = request.POST['mobno']
# 		password = request.POST['password']
# 		gender = request.POST['optradio']
# 		na = name.split(' ')
# 		l_name = ""
# 		f_name = ""
# 		print(na)
# 		for i in range(len(na)):
# 			if i == 0:
# 				f_name = na[i]
# 			else:
# 				l_name = l_name + na[i]+" "
# 		print(f_name,l_name)
# 		if not UserModel.objects.filter(email=email).exists():
# 			if not UserModel.objects.filter(mob_no=mobno).exists():
# 				UserModel(name=name, email=email, mob_no=mobno, password=password, gender=gender,
# 					f_name=f_name,l_name=l_name).save()
# 				messages.success(request, 'Successfully account created !')
# 				return redirect('login')
# 			else:
# 				messages.error(request, 'Entered mobile already exist !')
# 		else:
# 			messages.error(request, 'Entered email already exist !')
# 	return render(request, 'user/signup.html')
#
#
# def welcom_user(request):
# 	try:
# 		data = UserModel.objects.get(email=request.session["email"])
# 		context = {
# 		"data": data,
# 		"email":request.session["email"],
# 		}
# 		return render(request, "user/home.html", context)
# 	except:
# 		return redirect('login')
#
#
# def forgot_password(request):
# 	if request.method == 'POST':
# 		u_email=request.POST['u_email']
# 		if UserModel.objects.filter(email=u_email).exists():
# 			data = UserModel.objects.get(email=u_email)
# 			subject = "“Password of PG Booking”"
# 			message = f"Dear ({data.name}). Welcome to Booking PG. You are forgotten password. You are trying to recovery your password. We are care for our User. ({data.password}) is your password ."
# 			html_content = render_to_string("user/email_template.html", {'message': message})
# 			text_content = strip_tags(html_content)
# 			email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [u_email])
# 			email.attach_alternative(html_content, "text/html")
# 			email.send()
# 			messages.success(request, "Your password is send to your Email-id successfully !")
# 			return redirect('login')
# 		else:
# 			messages.error(request, "Enter a verified email-id !")
# 	return render(request, 'user/forgot_pass.html')
#
#
# def logout(request):
# 	try:
# 		del request.session["email"]
# 	except:
# 		return redirect('login')
# 	messages.success(request,"Successfully Logout !")
# 	return redirect('home')