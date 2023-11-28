from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Feature,Conformation
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from websiters.settings import EMAIL_HOST_USER
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
         username=request.POST['username']
         email=request.POST['email']
         password=request.POST['password']
         password2=request.POST['password2']
         if password==password2:
             if User.objects.filter(email=email).exists():
                 messages.info(request,'Email already exists')
                 return redirect('register')
             elif User.objects.filter(username=username).exists():
                 messages.info(request,'username already taken')
                 return redirect('register')
             else:
                 user =User.objects.create_user(username=username,
                                                email=email,password=password)
                 user.save()
                 return redirect('login')
         else:
             messages.info(request,'passwords mismatch')
             return render(request,'register.html')
    return render(request,'register.html')



def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
    
def style(request):
    return render(request,'style.css')
def logout(request):
    auth.logout(request)
    return redirect('/')

def DestinationDetails(request):
    if request.method == 'GET':
        query=request.GET.get('query')
        query1=request.GET.get('query1')
        routes=[]
        
        if query and query1:
    
            routes=Feature.objects.filter(fromdesti__icontains=query)
            routes=Feature.objects.filter(todesti__icontains=query1)
        if routes:   
            return render(request, 'Destinationdetails.html',{'routes':routes,'routes':routes})
        else:
            messages.info(request,"No routes found. Please search for other places.")
            return render(request, 'Destinationdetails.html', {'routes': []})

@login_required
def conformation(request):
    if request.method == 'POST':
        
        fromdesti = request.POST.get('fromdesti')
        todesti = request.POST.get('todesti')
        passenger_name = request.POST.get('passenger_name')
        email = request.POST.get('email')
        payment_mode = request.POST.get('payment_mode')
        print(passenger_name,email,payment_mode,f'Fromdesti: {fromdesti}, Todesti: {todesti}')
        # Assuming the user is logged in
        # user=request.user
        
        # Save booking details to the database
        Conformation.objects.create(
            # user_id_id=.user,
            user=request.user,
            from_location=fromdesti,
            to_location=todesti,
            passenger_name=passenger_name,
            email=email,
            payment_mode=payment_mode
        )
        # subject = 'Ticket Booking Confirmation'
        # html_message = render_to_string('booking_confirmation_email.html', {
        #     'passenger_name': passenger_name,
        #     'from_location': fromdesti,
        #     'to_location': todesti,
        # })
        # plain_message = strip_tags(html_message)
        # from_email = 'kasulaswagreddy4296@gmail.com'  # Replace with your email
        # to_email = [email]

        # send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
        send_mail("Thankyou for your Booking",f"{passenger_name} your Ticket is successfully booked...your destination details are {fromdesti} to {todesti}",EMAIL_HOST_USER,[email],fail_silently=True)
        return render(request, 'success.html', {
    'from_location': fromdesti,
    'to_location': todesti,
    'passenger_name': passenger_name,
    'email': email,
})
# Replace with the actual template name
    
    if request.user.is_authenticated:
        # If the user is already authenticated, proceed with the booking
        return render(request, 'conformation.html')
    messages.info(request, "Please create an account or log in to your account.")
    return render(request, 'register.html')


# Example using print statements
def your_view(request):
    fromdesti = request.POST.get('fromdesti')
    todesti = request.POST.get('todesti')
    print(f'From: {fromdesti}, To: {todesti}')
    # Rest of your view logic...

def tickets_view(request):
    # Logic to fetch user tickets from the database
    # Replace this with your actual logic
    user_tickets = Conformation.objects.filter(user=request.user)
    if user_tickets:
        return render(request, 'tickets.html', {'user_tickets': user_tickets})
    else:
        messages.info(request,"No Tickets found")
        return render(request, 'tickets.html')
        
def routes(request):
    features=Feature.objects.all()
    return render(request, 'routes.html',{'features':features})
