# -*- coding: utf-8 -*-
import operator,re
from django.shortcuts import render
from django.db.models import F,Q
from .models import Proposal
from search.models import Keyword
from search.views import keyword_list, keyword_been_searched
from issue.models import Issue


def proposal(request,proposal_id):
    proposal = Proposal.objects.select_related().get(uid=proposal_id)
    return render(request,'proposal/proposal.html', {'proposal': proposal})

def proposals(request,keyword_url):
    keyword,proposal,error = None,None,False
    if 'keyword' in request.GET:
        keyword = re.sub(u'[，。／＼、；］［＝－＜＞？：＂｛｝｜＋＿（）！＠＃％＄︿＆＊～~`!@#$%^&*_+-=,./<>?;:\'\"\[\]{}\|()]',' ',request.GET['keyword']).strip()
    elif keyword_url:
        keyword = keyword_url.strip()
    if keyword:
        proposal = Proposal.objects.filter(reduce(operator.and_, (Q(content__icontains=x) for x in keyword.split()))).order_by('-sitting__date')
        if proposal:
            keyword_been_searched(keyword, 1)
    else:
        proposal = Proposal.objects.all().order_by('-sitting__date')[:100]
    return render(request,'proposal/proposals.html', {'proposal':proposal,'keyword':keyword,'error':error,'keyword_obj':keyword_list(1)})
