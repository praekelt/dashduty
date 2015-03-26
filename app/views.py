import json
import time
from datetime import datetime, timedelta

from django.utils import timezone
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from app import models


@login_required
def index(request):
    return render(request, "index.html", {
        'key': settings.PAGERDUTY_KEY
    })
