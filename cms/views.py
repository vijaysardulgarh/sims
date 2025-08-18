from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from . import views
from .models import Staff,Student,Class,Subject,TimeSlot,News,SMCMember,School
# Create your views here.
import itertools

from django.db.models import Count, Q,Case, When
from cms.utils import generate_timetable

def timetable_view(request):
    # Fetch necessary data from the database
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    teachers = Staff.objects.all()
    time_slots = TimeSlot.objects.all()
    
    # Calculate total duration for the timetable (assuming 5 days a week)
    total_duration = 5 * 8  # 8 hours per day
    
    # Generate the timetable
    timetable = generate_timetable(classes, subjects, teachers, time_slots, total_duration)
    
    # Pass the timetable data to the template
    context = {'timetable': timetable}
    
    # Render the template
    return render(request, 'timetable.html', context)



def student_strength(request):

    if request.method == 'POST':
            # Get the school name from the form
            school_name = request.POST.get('school_name')
        

            class_order = {
                'Sixth': 1,
                'Seventh': 2,
                'Eighth': 3,
                'Nineth': 4,
                'Tenth': 5,
                'Eleventh': 6,    
                'Twelfth': 7,
            
            }

            student_strength = Student.objects.filter(school_name=school_name).values('studentclass', 'section','stream').annotate(
        
            scmale=Count('srn', filter=Q(gender='Male',category__in=['SC', 'Scheduled Caste'])),  
            scfemale=Count('srn', filter=Q(gender='Female',category__in=['SC', 'Scheduled Caste'])), 
            bcamale=Count('srn', filter=Q(gender='Male',category='BC-A')),  
            bcafemale=Count('srn', filter=Q(gender='Female',category='BC-A')),
            bcbmale=Count('srn', filter=Q(gender='Male',category='BC-B')),  
            bcbfemale=Count('srn', filter=Q(gender='Female',category='BC-B')),
            genmale=Count('srn', filter=Q(gender='Male',category__in=['GEN', 'General'])),  
            genfemale=Count('srn', filter=Q(gender='Female',category__in=['GEN', 'General'])),
            totalmale=Count('srn', filter=Q(gender='Male')),  
            totalfemale=Count('srn', filter=Q(gender='Female')),
            total=Count('srn'),
            #total_bpl=Count('srn', filter=Q(is_bpl=True)),
            malecwsn = Count('srn', filter=Q(gender='Male') & ~Q(disability=None) & ~Q(disability='')),
            femalecwsn = Count('srn', filter=Q(gender='Female') & ~Q(disability=None) & ~Q(disability='')),
            cwsn = Count('srn', filter=~Q(disability='') | ~Q(disability=None)),

            malebpl = Count('srn', filter=Q(gender='Male') & ~Q(bpl_certificate_issuing_authority=None) & ~Q(bpl_certificate_issuing_authority='')),
            femalebpl = Count('srn', filter=Q(gender='Female') & ~Q(bpl_certificate_issuing_authority=None) & ~Q(bpl_certificate_issuing_authority='')),
            bpl = Count('srn', filter=~Q(bpl_certificate_issuing_authority='') | ~Q(bpl_certificate_issuing_authority=None)),

            order=Case(*[When(studentclass=value, then=position) for value, position in class_order.items()])
        ).order_by('order')
            
            context = {
            #'sixth_sc_male':sixth_sc_male,
            #'sixth_sc_female_strength':sixth_sc_female_strength,
            #'seventh_sc_male_strength':seventh_sc_male_strength,
            #'seventh_sc_female_strength':seventh_sc_female_strength,
            #'eighth_sc_male_strength':eighth_sc_male_strength,
            #'eighth_sc_female_strength':eighth_sc_female_strength,
            #'student': student,
            'student_strength': student_strength,
            'school_name':school_name
        }
            return render(request, 'student_strength.html', context)

    else:
        school_names = Student.objects.values_list('school_name', flat=True).distinct()
        context = {'school_names': school_names}
        return render(request, 'school_student_strength.html',context)
    
def subject_strength(request):
    
   if request.method == 'POST':
            # Get the school name from the form
            school_name = request.POST.get('school_name')
        
            students =Student.objects.filter(school_name=school_name)      

            #for student in students:
                #subject_opted = student['subjects_opted']

            #    if student.subjects_opted:
            #        subject_list = student.subjects_opted.split(',')
            #        subjects = []
            #        for subject in subject_list:
            #            subject_type, subject_name = subject.split(':')
            #            subjects.append(subject_name.strip())


            class_order = {
                'Sixth': 1,
                'Seventh': 2,
                'Eighth': 3,
                'Nineth': 4,
                'Tenth': 5,
                'Eleventh': 6,    
                'Twelfth': 7,
            
            }

            subject_strength = Student.objects.filter(school_name=school_name).values('studentclass', 'section','stream').annotate(
        
            punjabi=Count('srn', filter=Q(subjects_opted__icontains='Punjabi')),  
            music=Count('srn', filter=Q(subjects_opted__icontains='Music')),  
            accountancy=Count('srn', filter=Q(subjects_opted__icontains='Accountancy')),  
            business_studies=Count('srn', filter=Q(subjects_opted__icontains='Business Studies')),  
            economics=Count('srn', filter=Q(subjects_opted__icontains='Economics')),

            sanskrit=Count('srn', filter=Q(subjects_opted__icontains='Sanskrit')),  
            fine_arts=Count('srn', filter=Q(subjects_opted__icontains='Fine Arts')),  
            political_science=Count('srn', filter=Q(subjects_opted__icontains='Political Science')),
            geography=Count('srn', filter=Q(subjects_opted__icontains='Geography')),    
            mathematics=Count('srn', filter=Q(subjects_opted__icontains='Mathematics')),  
            psychology=Count('srn', filter=Q(subjects_opted__icontains='Psychology')),
            drawing=Count('srn', filter=Q(subjects_opted__icontains='Drawing')),  
            english=Count('srn', filter=Q(subjects_opted__icontains='English')),  
            hindi=Count('srn', filter=Q(subjects_opted__icontains='Hindi')),  
            social_science=Count('srn', filter=Q(subjects_opted__icontains='Social Science')),  
            science=Count('srn', filter=Q(subjects_opted__icontains='Science')& ~Q(subjects_opted__icontains='Political Science')& ~Q(subjects_opted__icontains='Home Science')),
            physics=Count('srn', filter=Q(subjects_opted__icontains='Physics')),  
            chemistry=Count('srn', filter=Q(subjects_opted__icontains='Chemistry')),  
            biology=Count('srn', filter=Q(subjects_opted__icontains='Biology')),  
            home_science=Count('srn', filter=Q(subjects_opted__icontains='Home Science')),  
            physical_education=Count('srn', filter=Q(subjects_opted__icontains='Physical and Health Education') | Q(subjects_opted__icontains='Physical Education')),
            automobile=Count('srn', filter=Q(subjects_opted__icontains='Automotive')),  
            beauty_wellness=Count('srn', filter=Q(subjects_opted__icontains='Beauty & Wellness')),
           
            order=Case(*[When(studentclass=value, then=position) for value, position in class_order.items()])
        ).order_by('order')
            
            context = {

            'subject_strength': subject_strength,
            'school_name':school_name
        }
            return render(request, 'subject_strength.html', context)
   else:
        school_names = Student.objects.values_list('school_name', flat=True).distinct()
        context = {'school_names': school_names}
        return render(request, 'school_subject_strength.html',context)    
    
def index (request):
     
    school_name = 'PM Shri Government Senior Secondary School Nagpur'

    # Classes 6th to 8th
    lower_classes = ['Sixth', 'Seventh', 'Eighth']
    stats_lower = Student.objects.filter(
        school_name=school_name,
        studentclass__in=lower_classes
    ).aggregate(
        scmale=Count('srn', filter=Q(gender='Male', category__in=['SC', 'Scheduled Caste'])),
        scfemale=Count('srn', filter=Q(gender='Female', category__in=['SC', 'Scheduled Caste'])),
        bcamale=Count('srn', filter=Q(gender='Male', category='BC-A')),
        bcafemale=Count('srn', filter=Q(gender='Female', category='BC-A')),
        bcbmale=Count('srn', filter=Q(gender='Male', category='BC-B')),
        bcbfemale=Count('srn', filter=Q(gender='Female', category='BC-B')),
        genmale=Count('srn', filter=Q(gender='Male', category__in=['GEN', 'General'])),
        genfemale=Count('srn', filter=Q(gender='Female', category__in=['GEN', 'General'])),
    )

    # Classes 9th to 12th
    upper_classes = ['Nineth', 'Tenth', 'Eleventh', 'Twelfth']
    stats_upper = Student.objects.filter(
        school_name=school_name,
        studentclass__in=upper_classes
    ).aggregate(
        scmale=Count('srn', filter=Q(gender='Male', category__in=['SC', 'Scheduled Caste'])),
        scfemale=Count('srn', filter=Q(gender='Female', category__in=['SC', 'Scheduled Caste'])),
        bcamale=Count('srn', filter=Q(gender='Male', category='BC-A')),
        bcafemale=Count('srn', filter=Q(gender='Female', category='BC-A')),
        bcbmale=Count('srn', filter=Q(gender='Male', category='BC-B')),
        bcbfemale=Count('srn', filter=Q(gender='Female', category='BC-B')),
        genmale=Count('srn', filter=Q(gender='Male', category__in=['GEN', 'General'])),
        genfemale=Count('srn', filter=Q(gender='Female', category__in=['GEN', 'General'])),
    )
    teaching_staff = Staff.objects.filter(staff_role='Teaching').order_by('designation', 'name')
    
    # Non-Teaching staff grouped by designation
    non_teaching_staff = Staff.objects.filter(staff_role='Non-Teaching').order_by('designation', 'name')
    
    academic_news = News.objects.filter(category__iexact='Academics')[:10]
    event_news = News.objects.filter(category__iexact='Events')[:10]


    smcmembers = SMCMember.objects.all()



    context = {
        'stats_lower': stats_lower,
        'stats_upper': stats_upper,
        'school_name': school_name,
        'teaching_staff': teaching_staff,
        'non_teaching_staff': non_teaching_staff,
        'academic_news': academic_news,
        'event_news': event_news,
        'smcmembers': smcmembers
    }
    return render(request, 'index.html', context)

def student_strength1(request):
    # Fetch all distinct class names
    classes = Student.objects.values_list('studentclass', flat=True).distinct()

    # Fetch all distinct sections
    sections = Student.objects.values_list('section', flat=True).distinct()

    # Initialize a dictionary to hold statistics for each class and section combination
    class_section_statistics = {}

    # Iterate over each class and section combination
    for class_name in classes:
        for section in sections:
            # Filter students based on class and section
            students = Student.objects.filter(studentclass=class_name, section=section)

            # Calculate counts for each category and gender
            statistics = {
                'SC': {'Male': 0, 'Female': 0},
                'BC_A': {'Male': 0, 'Female': 0},
                'BC_B': {'Male': 0, 'Female': 0},
                'GEN': {'Male': 0, 'Female': 0},
                'Total': {'Male': 0, 'Female': 0},
                'CWSN': {'Male': 0, 'Female': 0},
                'BPL': {'Male': 0, 'Female': 0}
            }

            # Update counts based on the current student's category and gender
            for student in students:
                category_counts = statistics[student.category]
                category_counts[student.gender] += 1

            # Store statistics for the current class and section combination
            class_section_statistics[(class_name, section)] = statistics

    context = {
        'class_section_statistics': class_section_statistics
    }

    return render(request, 'student_strength.html', context)


def about (request):
    
    return render(request,"about.html",{})

def staff (request):
    staff_members=Staff.objects.all()
    return render(request,"staff_members.html",{'staff_members':staff_members})
    
def document_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    documents = school.documents.all()
    return render(request, "document_detail.html", {"school": school, "documents": documents})    


# Staff listing by role
def staff_by_role(request, role):
    staff_list = Staff.objects.filter(staff_role=role).order_by("name")
    return render(request, "staff_by_role.html", {
        "role": role,
        "staff_list": staff_list,
    })





