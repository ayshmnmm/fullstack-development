from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def contact_us(req):
    # context = {'form':ContactForm}
    # return render(req,'contactus.html',context)
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender','noreply@example.org')

            return HttpResponse(f"Thanks mate for your response on {topic}, we will respond to {sender} shortly.")
    else:
        form = ContactForm()

    return render(req, 'contactus.html', {'form':form})
