from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse


def start(request):
    return HttpResponse("<h1>Welcome ! Biu Dynamic Website Ready Programming ?</h1>")


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def medical(request):
    return render(request, 'courses/medical.html')


def dental(request):
    return render(request, 'courses/dental.html')


def nursing(request):
    return render(request, 'courses/nursing.html')


def pharmacy(request):
    return render(request, 'courses/pharmacy.html')


def management(request):
    return render(request, 'courses/management.html')


def humanitiesandjournalism(request):
    return render(request, 'courses/humanities&journalism.html')


def paramedical(request):
    return render(request, 'courses/paramedical.html')


def mbbs(request):
    return render(request, 'courses/mbbs.html')


def md(request):
    return render(request, 'courses/md.html')


def ms(request):
    return render(request, 'courses/ms.html')


def msc(request):
    return render(request, 'courses/msc.html')


def bds(request):
    return render(request, 'courses/bds.html')


def mds(request):
    return render(request, 'courses/mds.html')


def dh(request):
    return render(request, 'courses/dh.html')


def dm(request):
    return render(request, 'courses/dm.html')


def bscnursing(request):
    return render(request, 'courses/b.sc nursing.html')


def mscnursing(request):
    return render(request, 'courses/m.sc nursing.html')


def gnm(request):
    return render(request, 'courses/gnm.html')


def anm(request):
    return render(request, 'courses/anm.html')


def npcc(request):
    return render(request, 'courses/npcc.html')


def bpharma(request):
    return render(request, 'courses/bpharma.html')


def dpharma(request):
    return render(request, 'courses/dpharma.html')


def mha(request):
    return render(request, 'courses/mha.html')


def mph(request):
    return render(request, 'courses/mph.html')


def bbaft(request):
    return render(request, 'courses/bbaft.html')


def bcomh(request):
    return render(request, 'courses/bcomh.html')


def mcom(request):
    return render(request, 'courses/mcom.html')


def bsccs(request):
    return render(request, 'courses/bsccs.html')


def bajournalism(request):
    return render(request, 'courses/bajournalism.html')


def bamasscommunication(request):
    return render(request, 'courses/bamasscommunication.html')


def majournalism(request):
    return render(request, 'courses/majournalism.html')


def mamasscommunication(request):
    return render(request, 'courses/mamasscommunication.html')


def mapsychology(request):
    return render(request, 'courses/mapsychology.html')


def masociology(request):
    return render(request, 'courses/masociology.html')


def maenglish(request):
    return render(request, 'courses/maenglish.html')


def mahindi(request):
    return render(request, 'courses/mahindi.html')


def bpt(request):
    return render(request, 'courses/bpt.html')


def bscmlt(request):
    return render(request, 'courses/bscmlt.html')


def bscopt(request):
    return render(request, 'courses/bscopt.html')


def dmlt(request):
    return render(request, 'courses/dmlt.html')


def dxrt(request):
    return render(request, 'courses/dxrt.html')


def detc(request):
    return render(request, 'courses/detc.html')


def dsanitation(request):
    return render(request, 'courses/dsanitation.html')


def dialysistechnician(request):
    return render(request, 'courses/dialysistechnician.html')


def drit(request):
    return render(request, 'courses/drit.html')


def bscfc(request):
    return render(request, 'courses/bscfc.html')


def dmri(request):
    return render(request, 'courses/dmri.html')


def history(request):
    return render(request, 'history.html')


def infrastructure(request):
    return render(request, 'infrastructure.html')


def visionmission(request):
    return render(request, 'visionmission.html')


def facilities(request):
    return render(request, 'facilities.html')


def campus(request):
    return render(request, 'campus.html')


def universitylogo(request):
    return render(request, 'universitylogo.html')


def groupinstitute(request):
    return render(request, 'groupinstitute.html')


def journals(request):
    return render(request, 'journals.html')


def hospitals(request):
    return render(request, 'hospitals.html')


def events(request):
    return render(request, 'events.html')


def chancellor(request):
    return render(request, 'chancellor.html')


def vicechancellor(request):
    return render(request, 'vicechancellor.html')


def prochancellor(request):
    return render(request, 'prochancellor.html')


def provicechancellor(request):
    return render(request, 'provicechancellor.html')


def registrar(request):
    return render(request, 'registrar.html')


def underconstruction(request):
    return render(request, 'underconstruction.html')


def addmissionform(request):
    if request.method == 'POST':
        name = request.POST['form_name']
        email = request.POST['form_email']
        course = request.POST['form_course']
        mobile = request.POST['form_mobile']
        massage = request.POST['form_message']
        send_mail(
            'New Admission Enquiry',
            mobile,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return render(request, 'index.html')
