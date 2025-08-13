# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import reg,drreg,breg,lreg,labservice,pay,lbreg,labpay


from django.shortcuts import render,redirect
import razorpay #import this
from django.conf import settings
from django.http import HttpResponse

from django.http import JsonResponse #import this
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt #import this
from django.http import HttpResponseBadRequest #import this
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.
def index(request):
    return render(request,'index.html')
def indexp(request):
    return render(request,'indexp.html')
def indexd(request):
    return render(request,'indexd.html')
def lablog(request):
    return render(request,'lablog.html')
def testimonial(request):
    return render(request,'testimonial.html')
def contact(request):
    return render(request,'contact.html')
def feature(request):
    return render(request,'feature.html')

def logout(request):
    request.session.flush()
    return redirect('index')

def register(request):
    if request.method=="POST" :
        name = request.POST.get('name')
        pid = request.POST.get('pid')
        phno = request.POST.get('phno')
        email = request.POST.get('email')
        passw = request.POST.get('passw')
        cpassw = request.POST.get('cpassw')
        reg(name=name,pid=pid,phno=phno,passw=passw,cpassw=cpassw).save()
        return render(request,'index.html')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        passw = request.POST.get('passw')
        
        cr = reg.objects.filter(pid=pid, passw=passw)
        
        if cr.exists():
            user = cr.first()
            if user.status == "approved":
                request.session['pid'] = user.pid
                request.session['email'] = user.email
                return render(request, 'indexp.html')
            else:
                # If user status is not approved, render login form with custom error message
                return render(request, 'login.html', {'error_message': 'Your account is not approved.'})
        else:
            # If no matching record found, render login form with custom error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')

def profile(request):
    ownername=request.session['pid']
    cr=reg.objects.get(pid=ownername)
    name=cr.name
    patient_id=cr.pid
    phone_number=cr.phno
    password=cr.passw
    return render(request,'profile.html',{'name':name,'pid':patient_id,'phno':phone_number,'passw':password})

def profiled(request):
    ownername=request.session['did']
    cr=drreg.objects.get(did=ownername)
    dimage = cr.dimage
    dname=cr.dname
    ddep=cr.ddep
    did=cr.did
    fee=cr.fee
    demail=cr.demail
    phone_number=cr.dphn
    password=cr.dpass
    return render(request,'profiled.html',{'dimage':dimage,'dname':dname,'ddep':ddep,'did':did,'dphn':phone_number,'dpass':password,'fee':fee,'demail':demail})

def update(request):
    ownername=request.session['pid']
    cr=reg.objects.get(pid=ownername)
    name=cr.name
    patient_id=cr.pid
    phone_number=cr.phno
    password=cr.passw
    return render(request,'updateprofile.html',{'name':name,'pid':patient_id,'phno':phone_number,'passw':password})


def proupdate(request):
    ownername=request.session['pid']
    if request.method=="POST":
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        passw=request.POST.get('passw')

        data=reg.objects.get(pid=ownername)
        data.name=name
        data.phno=phno
        data.passw=passw
        data.save()
        return render(request,'index.html')
    else:
        return render(request,'updateprofile.html')

def dreg(request):
    if request.method=="POST" :
        dimage = request.FILES['dimage']
        dname = request.POST.get('dname')
        did = request.POST.get('did')
        ddep = request.POST.get('ddep')
        dphn = request.POST.get('dphn')
        fee = request.POST.get('fee')
        demail= request.POST.get('demail')
        dpass = request.POST.get('dpass')
        dpassre = request.POST.get('dpassre')
        drreg(dimage=dimage,dname=dname,did=did,demail=demail,ddep=ddep,dphn=dphn,fee=fee,dpass=dpass,dpassre=dpassre).save()
        return render(request,'indexd.html')
    else:
        return render(request,'dreg.html')
    
def dlog(request):
    if request.method=='POST':
        did=request.POST.get('did')
        dpass=request.POST.get('dpass')
        cr=drreg.objects.filter(did=did,dpass=dpass)
        if cr:
            user=drreg.objects.get(did=did,dpass=dpass)
            id=user.id
            did=user.did
            dpass=user.dpass
            request.session['did']=did
            # request.session['email']=cr.email
            return render(request,'indexd.html')
        else:
            return render(request,'dlogin.html')
    else:
        return render(request,'dlogin.html')
    
def listdr(request):
    cr=drreg.objects.all()
    return render(request,'listdr.html',{'a':cr})

def book(request):
    if request.method=='POST':
        id=request.POST.get('id')
        sd=drreg.objects.get(id=id)
        name=sd.dname
        phn=sd.dphn
        dep=sd.ddep
        did=sd.did
        fee=sd.fee
        pid=request.session['pid']
        cr=reg.objects.get(pid=pid)
        a=cr.name
        b=cr.pid
        c=cr.phno     
    return render(request,'booking.html',{'id':id,'name':a,'pid':b,'phno':c,'dname':name,'fee':fee,'dphn':phn,'ddep':dep,'did':did})

def booking(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pid= did=request.session['email']
        phno = request.POST.get('phno')
        dname = request.POST.get('dname')
        dphn = request.POST.get('dphn')
        did = request.POST.get('did')
        ddep = request.POST.get('ddep')
        fee = request.POST.get('fee')
        bdate = request.POST.get('bdate')
        btime = request.POST.get('btime')
        breg(name=name,email=pid,phno=phno,dname=dname,dphn=dphn,ddep=ddep,did=did,fee=fee,bdate=bdate,btime=btime).save()
        return render(request,'indexp.html')
    else:
        return render(request,'booking.html')
    
def listuser(request):
    did=request.session['did']
    cr=breg.objects.filter(did=did)
    return render(request,'listuser.html',{'a':cr})

def alog(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        passw = request.POST.get('apass')
        u = 'admin'
        p = 'admin'
        if uname==u:
            if passw==p:
                return render(request,'indexa.html')
            else:
                return render(request,"alog.html")
        else:
            return render(request,"alog.html")
    else:
        return render(request,"alog.html")

def alistusers(request):
    cr=reg.objects.all()
    return render(request,'alistusers.html',{'b':cr})

def alistdoctors(request):
    cr=drreg.objects.all()
    return render(request,'alistdoctors.html',{'c':cr})

def alistlab(request):
    cr=lreg.objects.all()
    return render(request,'alistlab.html',{'d':cr})

def lablog(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        passw = request.POST.get('lpass')
        u = 'kslab'
        p = 'kslab'
        if uname==u:
            if passw==p:
                return render(request,'indexl.html')
            else:
                return render(request,"lablog.html")
        else:
            return render(request,"lablog.html")
    else:
        return render(request,"lablog.html")
    
def ed(request,id):
    if request.method=='POST':
        # id=request.POST.get('id')
        sd=breg.objects.get(id=id)
        id=sd.id
        name=sd.name
        phno=sd.phno
        pid=sd.email   
        bdate=sd.bdate
        btime=sd.btime
        status=sd.status
    return render(request,'ed.html',{'id':id,'name':name,'pid':pid,'phno':phno,'bdate':bdate,'btime':btime,'status':status })

def update(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pid=request.POST.get('pid')
        phno = request.POST.get('phno')
        bdate = request.POST.get('bdate')
        btime = request.POST.get('btime')
        status = request.POST.get('status')
        id=request.POST.get('id')
        dt=breg.objects.get(id=id)
        dt.name=name
        dt.email=pid
        dt.phno=phno
        dt.bdate=bdate
        dt.btime=btime
        dt.status=status
        dt.save()
        return render(request,'indexd.html')
    
def mybookings(request):
    pid=request.session['email']
    print(pid)
    cr=breg.objects.filter(email=pid)
    return render(request,'mybookings.html',{'a':cr})

def labbook(request):
    pid=request.session['pid']
    cr=lbreg.objects.filter(pid=pid)
    return render(request,'labbook.html',{'a':cr})

def adupdate(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pid=request.POST.get('pid')
        phno = request.POST.get('phno')
        status = request.POST.get('status')
        id=request.POST.get('id')
        dt=reg.objects.get(id=id)
        dt.name=name
        dt.pid=pid
        dt.phno=phno
        dt.status=status
        dt.save()
        return render(request,'indexa.html')
    
def ad(request):
    if request.method=='POST':
        id=request.POST.get('id')
        sd=reg.objects.get(id=id)
        id=sd.id
        name=sd.name
        phno=sd.phno
        pid=sd.pid  
        status=sd.status
    return render(request,'ad.html',{'id':id,'name':name,'pid':pid,'phno':phno,'status':status})

def labservices(request):
    if request.method=="POST" :
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        time = request.POST.get('time')
        contact = request.POST.get('contact')
        labservice(category=category,price=price,description=description,contact=contact,time=time).save()
        return render(request,'indexl.html')
    else:
        return render(request,'labservices.html')
    
def labselect(request):
    cr=labservice.objects.all()
    return render(request,'labselect.html',{'a':cr})

def booklab(request):
    if request.method=='POST':
        id=request.POST.get('id')
        sd=labservice.objects.get(id=id)
        category=sd.category
        price=sd.price
        description=sd.description
        time=sd.time
        tokens=sd.tokens
        pid=request.session['pid']
        cr=reg.objects.get(pid=pid)
        a=cr.name
        b=cr.pid
        c=cr.phno    
    return render(request,'bookinglab.html',{'name':a,'pid':b,'phno':c,'category':category,'price':price,'description':description,'time':time,'tokens':tokens})

def bookinglab(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pid=request.POST.get('pid')
        phno = request.POST.get('phno')
        category=request.POST.get('category')
        price=request.POST.get('price')
        description = request.POST.get('description')
        time = request.POST.get('time')
        lbdate = request.POST.get('lbdate')
        tokens = request.POST.get('tokens')
        a=int(tokens)
        data=labservice.objects.get(category=category)
        b=data.tokens
        c=int(b)
        to=int(c-1)
        data.tokens=to
        data.save()
        lbreg(name=name,pid=pid,phno=phno,category=category,price=price,description=description,time=time,lbdate=lbdate,tokens=tokens).save()
        return render(request,'indexp.html')
    else:
        return render(request,'bookinglab.html')

def payment(request):
    pid=request.session['email']
    status="approved"
    cr=breg.objects.filter(email=pid,status=status)
    print("hello")
    print(cr)
    totalprice = 0
    if not cr.exists():
        return render(request,'your_template.html')
    
    
    for i in cr:
     pay(name=i.name, pid=i.email, phno=i.phno, bdate=i.bdate, did=i.did, dname=i.dname,dphn=i.dphn,ddep=i.ddep,fee=i.fee).save()
     totalprice += int(i.fee)
    #  i.delete()
    
    totalprice = int(totalprice*100)
    amount=int(totalprice)
    #amount=200
    print('amount is',str(amount))
    currency = 'INR'
    #amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request, 'Payment.html', context=context)



 
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'pay_success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'pay_failed.html')
            else:
 
                # if signature verification fails.
                return render(request, 'pay_failed.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    



def payment1(request):
    pid=request.session['pid']

    cr=lbreg.objects.filter(pid=pid)
    totalprice = 0
    # if not cr.exists():
    #     return render(request,'your_template.html')
    
    
    for i in cr:
     labpay(name=i.name,pid=i.pid,price=i.price,lbdate=i.lbdate,category=i.category,phno=i.phno).save()
     totalprice += int(i.price)
     i.delete()
    
    totalprice = int(totalprice*100)
    amount=int(totalprice)
    #amount=200
    print('amount is',str(amount))
    currency = 'INR'
    # amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler1/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request, 'payment1.html', context=context)


@csrf_exempt
def paymenthandler1(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                                        
                    # render success page on successful caputre of payment
                    return render(request, 'pay_success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'pay_failed.html')
            else:
 
                # if signature verification fails.
                return render(request, 'pay_failed.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    
def lablistusers(request):
    lb=labpay.objects.all()
    return render(request,'lablistusers.html',{'a':lb})

def uploadresult(request):
    if request.method=='POST':
        id=request.POST.get('id')
        sd=labpay.objects.get(id=id)
        id=sd.id
        # pid=sd.pid
        name=sd.name
        result=sd.result
    return render(request,'upload.html',{'id':id,'name':name,'result':result})

def upload(request):
    if request.method=='POST':
        name=request.POST.get('name')
        result = request.FILES['result']
        id=request.POST.get('id')
        dt=labpay.objects.get(id=id)
        dt.name=name
        dt.result=result
        dt.save()
        return render(request,'indexl.html')
  
def labresult(request):
    pid=request.session['pid']
    cr=labpay.objects.filter(pid=pid)
    return render(request,'labresult.html',{'a':cr})

def resultview(request):
    pid=request.session['pid']
    cr=labpay.objects.filter(pid=pid)
    return render(request,'resultview.html',{'a':cr})

def listpatients(request):
    lb=pay.objects.all()
    return render(request,'listpatients.html',{'a':lb})

def uploadpriscription(request):
    if request.method=='POST':
        id=request.POST.get('id')
        sd=pay.objects.get(id=id)
        id=sd.id
        name=sd.name
        priscription=sd.priscription
    return render(request,'uploadp.html',{'id':id,'name':name,'priscription':priscription})

def uploadp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        priscription = request.FILES['priscription']
        id=request.POST.get('id')
        dt=pay.objects.get(id=id)
        dt.name=name
        dt.priscription=priscription
        dt.save()
        return render(request,'indexd.html')

def priscription(request):
    p_id=request.session['pid']
    cr=pay.objects.filter(pid=p_id)
    return render(request,'priscription.html',{'a':cr})
  
def prisview(request,id):
    p_id=request.session['pid']
    cr=pay.objects.filter(id=id,pid=p_id)
    return render(request,'prisview.html',{'a':cr})


# Initialize Groq API client

from groq import Groq
client = Groq(api_key="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")
def chatbot(request):
    """ Renders the chatbot page """
    return render(request, "chatbot.html")
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot_api(request):
    """ Handles chatbot responses """
    if request.method == "POST":
        user_message = request.POST.get("message", "")

        if not user_message:
            return JsonResponse({"error": "No message provided"}, status=400)

        # Call Groq API
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_message}],
            temperature=0.7,
            max_completion_tokens=512,
            top_p=1,
        )

        response_text = completion.choices[0].message.content

        return JsonResponse({"response": response_text})

    return JsonResponse({"error": "Invalid request"}, status=400)
from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatMessage

def chat_list(request):
    farmers = drreg.objects.all()
    buyers = reg.objects.all()
    return render(request, 'chat_list.html', {'farmers': farmers, 'buyers': buyers})

from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatMessage

def chat_detail(request, user_type, user_email):
    sender_email = request.session.get('email')  # Assuming email is stored in the session

    if not sender_email:
        return redirect('login')  # Redirect to login if email is not in session

    # Identify the sender (Farmer or Buyer)
    sender = None
    if drreg.objects.filter(email=sender_email).exists():
        sender = drreg.objects.get(email=sender_email)
    elif reg.objects.filter(email=sender_email).exists():
        sender =  reg.objects.get(email=sender_email)

    if not sender:
        return redirect('login')  # Redirect if sender cannot be identified

    # Identify the receiver
    if user_type == 'farmer':
        receiver = get_object_or_404(drreg, email=user_email) 
    else:
        receiver = get_object_or_404(reg, email=user_email)

    # Fetch chat messages between sender and receiver using email
    messages = ChatMessage.objects.filter(
        sender__in=[sender.email, receiver.email],
        receiver__in=[sender.email, receiver.email]
    ).order_by('timestamp')

    # Handle sending a message
    if request.method == 'POST':
        content = request.POST.get('content')
        media = request.FILES.get('media')  # Fetch the media file from the form

        if content.strip() or media:
            ChatMessage.objects.create(
                sender=sender.email,
                receiver=receiver.email,
                content=content,
                media=media if media else None
            )

        return redirect('chat_detail', user_type=user_type, user_email=user_email)

    # Process media types for display
    for message in messages:
        if message.media:
            # Classify the media type (image or video)
            if message.media.name.endswith(('.jpg', '.jpeg', '.png')):
                message.media_type = 'image'
            elif message.media.name.endswith(('.mp4', '.avi', '.mov')):
                message.media_type = 'video'
            else:
                message.media_type = 'unknown'

    return render(request, 'chat_detail.html', {
        'receiver': receiver,
        'messages': messages,
        'sender': sender
    })

# def calculate_stock(bookings):
#     """Calculate the stock for each day based on the bookings.

#     Args:
#         bookings (list): List of bookings to consider. Each booking should
#             be a tuple containing the date, number of items booked, and
#             any other relevant information.

#     Returns:
#         list: List of tuples containing the date and stock level for
#             each day.
#     """
#     stock_by_day = {}
#     for booking in bookings:
#         date, num_booked = booking
#         if date not in stock_by_day:
#             stock_by_day[date] = 100  # initial stock level
#         stock_by_day[date] -= num_booked
#     # convert the dictionary to a list of tuples
#     stock\_by\_day\_list = list(stock\_by\_day.items())
#     return stock\_by\_day\_list

# bookings = [("2022-01-01", 5), ("2022-01-02", 10), ("2022-01-03", 2)]
# stock\_by\_day = calculate\_stock(bookings)
# for date, stock in stock\_by\_day:
#     # update the stock for the given date in the database
#     pass


# Videocall
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
import uuid
from .models import Appoint, Reg, Doctor, Payment


def initiate_video_call(request, appointment_id):
    """
    Initiates a video call for a specific appointment and sends an email to the patient
    with the link to join the call.
    """
    # Get the appointment object
    appointment = get_object_or_404(Appoint, id=appointment_id)
    
    # Generate a unique room ID using the appointment ID and a random UUID
    room_id = f"appt-{appointment_id}-{uuid.uuid4().hex[:8]}"
    
    # Create the video call link for the doctor
    doctor_call_url = request.build_absolute_uri(
        reverse('video_call') + f'?roomID={room_id}'
    )
    
    # Create the video call link for the patient
    patient_call_url = request.build_absolute_uri(
        reverse('video_call') + f'?roomID={room_id}'
    )
    
    # Get patient email
    patient_email = appointment.puser.email
    patient_name = appointment.puser.name
    doctor_name = appointment.doctor.name
    
    # Send email to the patient with the video call link
    subject = f"Video Consultation Link with Dr. {doctor_name}"
    message = f"""
    Dear {patient_name},
    
    Your video consultation with Dr. {doctor_name} has been scheduled.
    
    Date: {appointment.date}
    Time: {appointment.time}
    
    Please click on the link below to join the video call at the scheduled time:
    {patient_call_url}
    
    Best regards,
    Medical Center Team
    """
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[patient_email],
        fail_silently=False,
    )
    
    # Redirect the doctor to the video call page
    return redirect('video_call')

from django.http import JsonResponse

def video_call(request):
    """Render the video call page"""
    id = request.session.get('email')
    
    # Get the user's name based on session
    if id:
        try:
            user = Doctor.objects.get(email=id)
            user_name = user.name
        except:

            user = Reg.objects.get(email=id)
            user_name = user.name
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
        
    context = {
        'user_name': user_name
    }
    return render(request, 'videocall.html', context)