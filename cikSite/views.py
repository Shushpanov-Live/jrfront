from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import VotingForm, UploadFileForm
from django.views.generic import DetailView, ListView
from datetime import datetime
import aspose.words as aw
from django.core.files.storage import FileSystemStorage
from my_voice.settings import MEDIA_ROOT
from docxtpl import DocxTemplate
from django.http import FileResponse
import os
import mimetypes


def test(self, request):
    base_url = MEDIA_ROOT + '/user/user_template/'
    asset_url = base_url + 'test template.docx'
    tpl = DocxTemplate(asset_url)
    context = {'tema': 'Хахаха, а вот и'}
    tpl.render(context)
    tpl.save(base_url + 'test.docx')
    return render(request, "cikSite/cik.html", context)


def cik(request):
    return render(request, 'cikSite/cik.html')

def newwapon(request):
    error = ''
    if request.method == 'POST':
        title = request.POST.get('title', '')
        time = request.POST.get('time', '')
        kuda = request.POST.get('kuda', '')
        komy = request.POST.get('komy', '')
        email = request.POST.get('email', '')
        base_url = MEDIA_ROOT + '/user/user_template/'
        asset_url = base_url + 'test template.docx'
        tpl = DocxTemplate(asset_url)
        context = {'title': title, 'time': time, 'kuda': kuda, 'komy': komy, 'email': email}
        tpl.render(context)
        tpl.save(base_url + 'test.docx')

        filename = 'test.docx'
        filepath = MEDIA_ROOT + '/user/user_template/' + filename
        # path = open(filepath, 'rb')
        # mime_type, _ = mimetypes.guess_type(filepath)
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        response = FileResponse(open(filepath, 'rb'))
        return response

    form = VotingForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request,'cikSite/newwapon.html', date)
    
def dogovordog(request):
    error = ''
    if request.method == 'POST':
        number = request.POST.get('number', '')
        nameclient = request.POST.get('nameclient', '')
        data1 = request.POST.get('data1', '')
        data2 = request.POST.get('data2', '')
        base_url = MEDIA_ROOT + '/user/user_template/'
        asset_url = base_url + 'dogovordog.docx'
        tpl = DocxTemplate(asset_url)
        context = {'number': number, 'nameclient': nameclient, 'data1': data1, 'data2': data2}
        tpl.render(context)
        tpl.save(base_url + 'test.docx')

        filename = 'test.docx'
        filepath = MEDIA_ROOT + '/user/user_template/' + filename
        # path = open(filepath, 'rb')
        # mime_type, _ = mimetypes.guess_type(filepath)
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        response = FileResponse(open(filepath, 'rb'))
        return response

    form = VotingForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request,'cikSite/dogovordog.html', date)

def raspiska_o_zaeme(request):
    error = ''
    if request.method == 'POST':
        namer = request.POST.get('namer', '')
        city = request.POST.get('city', '')
        moneygive = request.POST.get('moneygive', '')
        summa = request.POST.get('summa', '')
        name = request.POST.get('name', '')
        times = request.POST.get('time', '')
        day = times[8:]
        mounth = times[5:7]
        base_url = MEDIA_ROOT + '/user/user_template/'
        asset_url = base_url + 'raspiska_o_zaeme_template.docx'
        tpl = DocxTemplate(asset_url)
        context = {'namer': namer, 'city': city, 'moneygive': moneygive, 'summa': summa, 'name': name, 'day': day, 'mounth': mounth,}
        tpl.render(context)
        tpl.save(base_url + 'test.docx')

        filename = 'test.docx'
        filepath = MEDIA_ROOT + '/user/user_template/' + filename
        # path = open(filepath, 'rb')
        # mime_type, _ = mimetypes.guess_type(filepath)
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        response = FileResponse(open(filepath, 'rb'))
        return response

    form = VotingForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request,'cikSite/raspiska_o_zaeme.html', date)


def doverennost(request):
    error = ''
    if request.method == 'POST':
        grazhA = request.POST.get('grazhA', '')
        adresnA = request.POST.get('adresnA', '')
        grazhB = request.POST.get('grazhB', '')
        adresnB = request.POST.get('adresnB', '')
        docker = request.POST.get('docker', '')
        organaiz = request.POST.get('organaiz', '')
        town = request.POST.get('town', '')
        newdata = request.POST.get('newdata', '')
        base_url = MEDIA_ROOT + '/user/user_template/'
        asset_url = base_url + 'doverennost_template.docx'
        tpl = DocxTemplate(asset_url)
        context = {'grazhA': grazhA, 'adresnA': adresnA, 'grazhB': grazhB, 'adresnB': adresnB, 'docker': docker,
                   'organaiz': organaiz, 'town': town, 'newdata': newdata,}
        tpl.render(context)
        tpl.save(base_url + 'test.docx')

        filename = 'test.docx'
        filepath = MEDIA_ROOT + '/user/user_template/' + filename
        # path = open(filepath, 'rb')
        # mime_type, _ = mimetypes.guess_type(filepath)
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        response = FileResponse(open(filepath, 'rb'))
        return response

    form = VotingForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request,'cikSite/doverennost.html', date)


def akt_vypolnennyh_rabot(request):
    error = ''
    if request.method == 'POST':
        nomber = request.POST.get('nomber', '')
        nameIsp = request.POST.get('nameIsp', '')
        nameZak = request.POST.get('nameZak', '')
        cena = request.POST.get('cena', '')
        cenaNDS = request.POST.get('cenaNDS', '')
        newdata = request.POST.get('newdata', '')
        data = newdata[8:]
        mont = newdata[5:7]
        yaer = newdata[2:4]
        base_url = MEDIA_ROOT + '/user/user_template/'
        asset_url = base_url + 'akt_vypolnennyh_rabot_template.docx'
        tpl = DocxTemplate(asset_url)
        context = {'nomber': nomber, 'nameIsp': nameIsp, 'nameZak': nameZak, 'cena': cena, 'cenaNDS': cenaNDS,
                   'data': data, 'mont': mont, 'yaer': yaer,}
        tpl.render(context)
        tpl.save(base_url + 'test.docx')

        filename = 'test.docx'
        filepath = MEDIA_ROOT + '/user/user_template/' + filename
        # path = open(filepath, 'rb')
        # mime_type, _ = mimetypes.guess_type(filepath)
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        response = FileResponse(open(filepath, 'rb'))
        return response

    form = VotingForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request,'cikSite/akt_vypolnennyh_rabot.html', date)


def spravka(request):
    error = ''
    if request.method == 'POST':
        grazdan = request.POST.get('grazdan', '')
        adress = request.POST.get('adress', '')
        yer = request.POST.get('yer', '')
        dateA = request.POST.get('dateA', '')
        dateB = request.POST.get('dateB', '')
        job = request.POST.get('job', '')
        dateC = request.POST.get('dateC', '')
        base_url = MEDIA_ROOT + '/user/user_template/'
        asset_url = base_url + 'spravka_template.docx'
        tpl = DocxTemplate(asset_url)
        context = {'grazdan': grazdan, 'adress': adress, 'yer': yer, 'dateA': dateA, 'dateB': dateB,
                   'job': job, 'dateC': dateC,}
        tpl.render(context)
        tpl.save(base_url + 'test.docx')

        filename = 'test.docx'
        filepath = MEDIA_ROOT + '/user/user_template/' + filename
        # path = open(filepath, 'rb')
        # mime_type, _ = mimetypes.guess_type(filepath)
        # response = HttpResponse(path, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        response = FileResponse(open(filepath, 'rb'))
        return response

    form = VotingForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request,'cikSite/spravka.html', date)

def comparison(request):
    if request.method == 'POST':
        myfileA = request.FILES['docA']
        myfileB = request.FILES['docB']
        fs = FileSystemStorage()

        base_url = MEDIA_ROOT + '/'

        filenameA = fs.save(myfileA.name, myfileA)
        filenameB = fs.save(myfileB.name, myfileB)
        uploaded_file_url = fs.url(filenameA)

        filepathA = MEDIA_ROOT + '/' + filenameA
        filepathB = MEDIA_ROOT + '/' + filenameB

        docA = aw.Document(filepathA)
        docB = aw.Document(filepathB)
        # There should be no revisions before comparison.
        docA.accept_all_revisions()
        docB.accept_all_revisions()
        docA.compare(docB, "Author Name", datetime.now())
        docA.save(base_url + 'Output.docx')

        filepath = MEDIA_ROOT + '/' + 'Output.docx'


        response = FileResponse(open(filepath, 'rb'))
        return response
    return render(request, 'cikSite/comparison.html')
