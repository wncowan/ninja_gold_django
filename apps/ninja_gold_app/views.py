# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print(request.session)


    if 'gold' not in request.session:
        print('no gold')
        request.session['gold'] = 0
        print(request.session['gold'])
    if 'activities' not in request.session:
        print('no activities')
        request.session['activities'] = []
        print(request.session['activities'])
    return render(request, "ninja_gold_app/index.html")

def process(request):
    if request.method == "POST":
        place = request.POST['name']
        if place == 'farm':
            print('made it to farm')
            payout = randint(10,20)
            request.session['gold'] += payout
            at_time = strftime("%Y-%m-%d %H:%M %p", gmtime())  
            request.session['activities'].append('copped {} from {} at time {}'.format(payout, place, at_time))
        if place == 'cave':
            payout = randint(5,10)
            request.session['gold'] += payout
            at_time = strftime("%Y-%m-%d %H:%M %p", gmtime())  
            request.session['activities'].append('copped {} from {} at time {}'.format(payout, place, at_time))
        if place == 'house':
            payout = randint(2,5)
            request.session['gold'] += payout
            at_time = strftime("%Y-%m-%d %H:%M %p", gmtime())  
            request.session['activities'].append('copped {} from {} at time {}'.format(payout, place, at_time))
        if place == 'casino':
            payout = randint(-50,50)
            request.session['gold'] += payout
            if payout < 0:
                at_time = strftime("%Y-%m-%d %H:%M %p", gmtime())  
                request.session['activities'].append('wasted {} at {} at time {}'.format(payout, place, at_time))
            else:
                at_time = strftime("%Y-%m-%d %H:%M %p", gmtime())  
                request.session['activities'].append('copped {} from {} at time {}'.format(payout, place, at_time))
        return redirect('/')

def delete(request):
    if request.method == "POST":
        print('entered delete route')
        del request.session['gold']
        del request.session['activities']
    return redirect('/')
