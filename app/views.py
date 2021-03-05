from django.shortcuts import render
import json
from django.http import HttpRequest,HttpResponse,JsonResponse
from .models import train_user as user
from .models import match_results as results
from django.db.models import Q


# Create your views here.


def index(request):
    if request.method == 'GET':
        data = {'power': ''}
        d = request.GET
        nickname = d['nickname']
        res = user.objects.filter(nickname=nickname)
        if res:
            power = res[0].power
            data['power'] = power
            if power == '2':
                jf = res[0].jifen
                zzjg = res[0].zzjg
                r1 = user.objects.all().filter(zzjg=zzjg).order_by('-jifen')
                n = 0
                while n < len(r1):
                    if r1[n].nickname == nickname:
                        pm = n + 1
                    n += 1
                data['jf'] = jf
                data['pm'] = pm
        else:
            data['power'] = ''
        response = HttpResponse(json.dumps(data))
        return response


def input(request):
    if request.method == 'POST':
        data = {'msg': ''}
        d = request.POST
        m = results()
        m.a1 = d['a1']
        m.a2 = d['a2']
        m.b1 = d['b1']
        m.b2 = d['b2']
        m.zongbifen = d['zbf']
        m.meijubifen = d['mjbf']
        m.shengli1 = d['s1']
        m.shengli2 = d['s2']
        m.project = d['project']
        m.save()
        if d['s1'] != '':
            u1 = user.objects.get(name=d['s1'])
            if u1.jifen == None:
                u1.jifen = 3
            else:
                u1.jifen += 3
            u1.save()
        if d['s2'] != '':
            u2 = user.objects.get(name=d['s2'])
            if u2.jifen == None:
                u2.jifen = 3
            else:
                u2.jifen += 3
            u2.save()
        data['msg'] = '提交成功'
        response = HttpResponse(json.dumps(data))
        return response

    return HttpResponse


def list(request):
    if request.method == 'GET':
        data = {'data': []}

        nickname = request.GET['nickname']
        zzjg = user.objects.filter(nickname=nickname)[0].zzjg
        z1 = zzjg.replace('，', ',').replace(' ', '')
        z2 = z1.split(',')
        dl = []
        for z in z2:
            res = results.objects.filter(project=z[:2])
            for p in res:
                dl.append(p)
        for i in dl:
            a2 = i.a2
            b2 = i.b2
            s2 = i.shengli2
            if len(a2) > 0:
                a2 = '-' + a2
            if len(b2) > 0:
                b2 = '-' + b2
            if len(s2) > 0:
                s2 = '-' + s2
            d = {
                'a1': i.a1,
                'a2': a2,
                'b1': i.b1,
                'b2': b2,
                'zbf': i.zongbifen,
                'mjbf': i.meijubifen,
                's1': i.shengli1,
                's2': s2,
            }
            data['data'].append(d)
        data['data'].reverse()
        response = HttpResponse(json.dumps(data))
        return response


def setuser(request):
    if request.method == 'POST':
        data = {'msg': ''}
        d = request.POST
        u = user()
        u.nickname = d['nickname']
        u.name = d['name']
        u.power = d['power']
        u.zzjg = d['zzjg']
        u.save()
        response = HttpResponse(json.dumps(data))
        return response

    return HttpResponse


def jfpm(request):
    if request.method == 'GET':
        data = {'data': []}

        nickname = request.GET['nickname']
        zzjg = user.objects.filter(nickname=nickname)[0].zzjg
        z1 = zzjg.replace('，', ',').replace(' ', '')
        z2 = z1.split(',')
        dl = []
        for z in z2:
            res = user.objects.filter(Q(zzjg=z) & Q(power='2')).order_by('-jifen')
            n = 0
            while n < len(res):
                player_info = [res[n].name, res[n].jifen, n+1, res[n].zzjg[:2]]
                dl.append(player_info)
                n += 1
        data['data'] = dl
        response = HttpResponse(json.dumps(data))
        return response
