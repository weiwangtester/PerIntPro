#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

def fun_views(request):
	return HttpResponse("Hello Django")
