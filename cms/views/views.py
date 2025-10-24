

import csv
#import datetime
#from datetime import datetime
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q, Case, When,Sum,OuterRef,IntegerField,Value,CharField
from django.http import FileResponse, Http404
from django.utils.timezone import now
from reportlab.lib.pagesizes import legal, landscape
from .utils import get_current_school
from .models import (
    Staff, Student, Class, Subject,MandatoryPublicDisclosure,Timetable,TimetableSlot,Classroom,Day,School,ClassIncharge,
    News, SMCMember, Committee, School,FeeStructure,FAQ,ClassSubject,Section,TeacherSubjectAssignment,TeacherAttendance,
    AboutSchool, Principal, Affiliation,StaffAssociationRoleAssignment, Association,StudentAchievement,Infrastructure,SanctionedPost
   
)
from collections import defaultdict
from cms.utils import generate_timetable
from django.core.exceptions import ValidationError
import itertools
from django.db.models import Prefetch
import os
from django.conf import settings
# -------------------- Utility --------------------
from django.db.models import F
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import Student
import io
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from reportlab.platypus import Spacer
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.dateparse import parse_date
from django.utils import timezone
import re
from .enrollment_subjects_utils import convert_subjects_to_cbse_slots, MEDIUM_CODE_MAP,get_medium_from_section
# -------------------- Dashboard & Common --------------------



from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle



from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors



from collections import defaultdict
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

from collections import defaultdict
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet


from django.shortcuts import render, redirect



# ✅ Show available class-section links



from .enrollment_subjects_utils import get_student_cbse_subjects, get_medium_from_section
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont





