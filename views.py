from django.shortcuts import render
import requests

def rest(request):
    response = requests.get('http://10.10.4.214:9001/ords/apex_ebs_extension/fams/support/')
    famsdata = response.json()
    return render(request, 'core/home.html', {
        'ticket_no': famsdata['support_ticket_no'],
        'description': famsdata['support_description'],
        'category': famsdata['support_category'],
        'status': famsdata['status'],
        'email': famsdata['contact_email']
    })