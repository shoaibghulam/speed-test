from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.start, name='start'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('stream/medical', views.medical, name='medical'),
    path('stream/dental', views.dental, name='dental'),
    path('stream/nursing', views.nursing, name='nursing'),
    path('stream/pharmacy', views.pharmacy, name='pharmacy'),
    path('stream/management', views.management, name='management'),
    path('stream/humanitiesandjournalism', views.humanitiesandjournalism, name='humanitiesandjournalism'),
    path('stream/paramedical', views.paramedical, name='paramedical'),
    path('courses/mbbs', views.mbbs, name='mbbs'),
    path('courses/md', views.md, name='md'),
    path('courses/ms', views.ms, name='ms'),
    path('courses/msc', views.msc, name='msc'),
    path('courses/bds', views.bds, name='bds'),
    path('courses/mds', views.mds, name='mds'),
    path('courses/dh', views.dh, name='dh'),
    path('courses/dm', views.dm, name='dm'),
    path('courses/bscnursing', views.bscnursing, name='bscnursing'),
    path('courses/mscnursing', views.mscnursing, name='mscnursing'),
    path('courses/anm', views.anm, name='anm'),
    path('courses/npcc', views.npcc, name='npcc'),
    path('courses/gnm', views.gnm, name='gnm'),
    path('courses/dpharma', views.dpharma, name='D.Pharma'),
    path('courses/bpharma', views.bpharma, name='B.Pharma'),
    path('courses/mha', views.mha, name='MHA'),
    path('courses/mph', views.mph, name='MPh'),
    path('courses/bbaft', views.bbaft, name='bbaft'),
    path('courses/bcomh', views.bcomh, name='bcomh'),
    path('courses/bsccs', views.bsccs, name='bsccs'),
    path('courses/mcom', views.mcom, name='mcom'),
    path('courses/bajournalism', views.bajournalism, name='bajournalism'),
    path('courses/bamasscommunication', views.bamasscommunication, name='bamasscommunication'),
    path('courses/majournalism', views.majournalism, name='majournalism'),
    path('courses/mamasscommunication', views.mamasscommunication, name='mamasscommunication'),
    path('courses/mapsychology', views.mapsychology, name='mapsychology'),
    path('courses/masociology', views.masociology, name='masociology'),
    path('courses/maenglish', views.maenglish, name='maenglish'),
    path('courses/mahindi', views.mahindi, name='mahindi'),
    path('courses/bpt', views.bpt, name='bpt'),
    path('courses/bscmlt', views.bscmlt, name='bscmlt'),
    path('courses/bscopt', views.bscopt, name='bscopt'),
    path('courses/bscfc', views.bscfc, name='bscfc'),
    path('courses/dmlt', views.dmlt, name='dmlt'),
    path('courses/dxrt', views.dxrt, name='dxrt'),
    path('courses/detc', views.detc, name='detc'),
    path('courses/dsanitation', views.dsanitation, name='dsanitation'),
    path('courses/dialysistechnician', views.dialysistechnician, name='dialysistechnician'),
    path('courses/dmri', views.dmri, name='dmri'),
    path('courses/drit', views.drit, name='drit'),
    path('history', views.history, name='history'),
    path('infrastructure', views.infrastructure, name='infrastructure'),
    path('visionmission', views.visionmission, name='visionmission'),
    path('facilities', views.facilities, name='facilities'),
    path('campus', views.campus, name='campus'),
    path('universitylogo', views.universitylogo, name='universitylogo'),
    path('groupinstitute', views.groupinstitute, name='groupinstitute'),
    path('journals', views.journals, name='journals'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('events', views.events, name='events'),
    # urls for home filters
    # Medical
    path('courses/md(anatomy)', views.md, name='md'),
    path('courses/md(anaesthesiology)', views.md, name='md'),
    path('courses/md(biochemistry)', views.md, name='md'),
    path('courses/md(respiratorymedicine)', views.md, name='md'),
    path('courses/md(communitymedicine)', views.md, name='md'),
    path('courses/md(dermatology)', views.md, name='md'),
    path('courses/md(generalmedicine)', views.md, name='md'),
    path('courses/md(microbiology)', views.md, name='md'),
    path('courses/md(paediatrics)', views.md, name='md'),
    path('courses/md(pharmacology)', views.md, name='md'),
    path('courses/md(physiology)', views.md, name='md'),
    path('courses/md(psychiatry)', views.md, name='md'),
    path('courses/md(radiodiagnosis)', views.md, name='md'),
    path('courses/ms(e.n.t.)', views.ms, name='ms'),
    path('courses/ms(generalsurgery)', views.ms, name='ms'),
    path('courses/ms(obst.&gynaeco)', views.ms, name='ms'),
    path('courses/ms(ophthalmology)', views.ms, name='ms'),
    path('courses/ms(orthopaedics)', views.ms, name='ms'),
    path('courses/m.sc.anatomy', views.msc, name='msc'),
    path('courses/m.sc.physiology', views.msc, name='msc'),
    path('courses/m.sc.biochemistry', views.msc, name='msc'),
    path('courses/m.sc.pharmacology', views.msc, name='msc'),
    path('courses/m.sc.microbiology', views.msc, name='msc'),
    # Dental
    path('courses/mds(conservativedentistry&endodontics)', views.mds, name='mds'),
    path('courses/mds(oral&maxillofacialsurgery', views.mds, name='mds'),
    path('courses/mds(orthodontics)', views.mds, name='mds'),
    path('courses/mds(periodontics)', views.mds, name='mds'),
    path('courses/mds(prosthodonticsandcrown&bridge)', views.mds, name='mds'),
    path('courses/mds(oralmedicineandradiology)', views.mds, name='mds'),
    path('courses/mds(paediatric&preventivedentistry', views.mds, name='mds'),
    path('courses/mds(publichealthdentistry)', views.mds, name='mds'),
    path('courses/mds(oralpathology&microbiology)', views.mds, name='mds'),
    path('courses/diplomaindentalhygienist', views.dh, name='dh'),
    path('courses/diploma-dentalmechanics', views.dm, name='dm'),
    # Management
    path('courses/mastershospitaladministration', views.mha, name='MHA'),
    path('courses/masterinpublichealth', views.mph, name='MPh'),
    path('courses/bba(finance&taxation)', views.bbaft, name='bbaft'),
    path('courses/b.com(hons)', views.bcomh, name='bcomh'),
    path('courses/b.sc(computerscience)', views.bsccs, name='bsccs'),
    # Paramedical
    path('courses/bsc.(optometry)', views.bscopt, name='bscopt'),
    path('courses/bsc(forensicsciences)', views.bscfc, name='bscfc'),
    path('courses/diplomainmlt', views.dmlt, name='dmlt'),
    path('courses/diplomainx-raytechnician', views.dxrt, name='dxrt'),
    path('courses/diplomainemergency&traumacare', views.detc, name='detc'),
    path('courses/diplomainsanitation', views.dsanitation, name='dsanitation'),
    path('courses/diplomaindialysistechnician', views.dialysistechnician, name='dialysistechnician'),
    path('courses/diplomainmritechnician', views.dmri, name='dmri'),
    path('courses/diplomainradioimagingtechnology', views.drit, name='drit'),
    # Phd.
    path('courses/medicalsciences(specializations)', views.underconstruction, name='underconstruction'),
    path('courses/dentalsciences(specializations)', views.underconstruction, name='underconstruction'),
    path('courses/nursingsciences(specializations)', views.underconstruction, name='underconstruction'),
    path('courses/pharmacysciences(specializations)', views.underconstruction, name='underconstruction'),
    path('courses/paramedicalsciences(specializations)', views.underconstruction, name='underconstruction'),
    # Finish
    path('chancellor', views.chancellor, name='chancellor'),
    path('vicechancellor', views.vicechancellor, name='vicechancellor'),
    path('prochancellor', views.prochancellor, name='prochancellor'),
    path('provicechancellor', views.provicechancellor, name='provicechancellor'),
    path('registrar', views.registrar, name='registrar'),
    path('addmissionform', views.addmissionform, name='addmissionform'),

    # path(r'^/courses/$', views.courses),
]
