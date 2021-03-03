from django.shortcuts import render
import json
from django.http import HttpRequest,HttpResponse,JsonResponse
from .models import train_user as user
from .models import match_results as results

# Create your views here.


def index(request):
    if request.method == 'GET':
        data = {'power': ''}
        d = request.GET
        nickname = d['nickname']
        res = user.objects.get(nickname=nickname)
        power = res.power
        data['power'] = power
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
        res = results.objects.all()
        for i in res:
            d = {
                'a1': i.a1,
                'a2': i.a2,
                'b1': i.b1,
                'b2': i.b2,
                'zbf': i.zongbifen,
                'mjbf': i.meijubifen,
                's1': i.shengli1,
                's2': i.shengli2,
            }
            data['data'].append(d)
        tt = {
            'a1': '对阵双方',
            'a2': '',
            'b1': '',
            'b2': '',
            'zbf': '总比分',
            'mjbf': '每局比分',
            's1': '获胜球员',
            's2': '',
        }
        data['data'].reverse()
        response = HttpResponse(json.dumps(data))
        return response



