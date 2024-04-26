from django.shortcuts import render
from . import views
from .models import Staff,Student
# Create your views here.
import itertools

from django.db.models import Count, Q,Case, When

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

            student_strength = Student.objects.filter(school_name=school_name).values('studentclass', 'section',).annotate(
        
            scmale=Count('srn', filter=Q(gender='Male',category__in=['SC', 'Scheduled Caste'])),  
            scfemale=Count('srn', filter=Q(gender='Female',category__in=['SC', 'Scheduled Caste'])), 
            bcamale=Count('srn', filter=Q(gender='Male',category='BC-A')),  
            bcafemale=Count('srn', filter=Q(gender='Female',category='BC-A')),
            bcbmale=Count('srn', filter=Q(gender='Male',category='BC-B')),  
            bcbfemale=Count('srn', filter=Q(gender='Female',category='BC-B')),
            genmale=Count('srn', filter=Q(gender='Male',category='GEN')),  
            genfemale=Count('srn', filter=Q(gender='Female',category='GEN')),
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
    
def index (request):
     
    staff_members=Staff.objects.all

    sc_Male_count = Student.objects.filter(category='SC', gender='Male').count()
    sc_Female_count = Student.objects.filter(category='SC', gender='Female').count()
    total_sc_students_count = Student.objects.filter(category='SC').count()

    bca_Male_count = Student.objects.filter(category='BCA', gender='Male').count()
    bca_Female_count = Student.objects.filter(category='BCA', gender='Female').count()
    total_bca_students_count = Student.objects.filter(category='BCA').count()

    bcb_Male_count = Student.objects.filter(category='BCB', gender='Male').count()
    bcb_Female_count = Student.objects.filter(category='BCB', gender='Female').count()
    total_bcb_students_count = Student.objects.filter(category='BCB').count()

    gen_Male_count = Student.objects.filter(category='General', gender='Male').count()
    gen_Female_count = Student.objects.filter(category='General', gender='Female').count()
    total_gen_students_count = Student.objects.filter(category='General').count()

    sc_male_teachers_count = Staff.objects.filter(category='SC', gender='Male').count()
    sc_female_teachers_count = Staff.objects.filter(category='SC', gender='Female').count()
    total_sc_teachers_count = Staff.objects.filter(category='SC').count()

    bca_male_teachers_count = Staff.objects.filter(category='BC-A', gender='Male').count()
    bca_female_teachers_count = Staff.objects.filter(category='BC-A', gender='Female').count()
    total_bca_teachers_count = Staff.objects.filter(category='BC-A').count()

    bcb_male_teachers_count = Staff.objects.filter(category='BC-B', gender='Male').count()
    bcb_female_teachers_count = Staff.objects.filter(category='BC-B', gender='Female').count()
    total_bcb_teachers_count = Staff.objects.filter(category='BC-B').count()

    gen_male_teachers_count = Staff.objects.filter(category='GEN', gender='Male').count()
    gen_female_teachers_count = Staff.objects.filter(category='GEN', gender='Female').count()
    total_gen_teachers_count = Staff.objects.filter(category='GEN').count()

    context = {
        'staff_members':staff_members,
        'sc_Male_count': sc_Male_count,
        'sc_Female_count': sc_Female_count,
        'total_sc_students_count': total_sc_students_count,
        'bca_Male_count': bca_Male_count,
        'bca_Female_count': bca_Female_count,
        'total_bca_students_count': total_bca_students_count,
        'bcb_Male_count': bcb_Male_count,
        'bcb_Female_count': bcb_Female_count,
        'total_bcb_students_count': total_bcb_students_count,
        'gen_Male_count': gen_Male_count,
        'gen_Female_count': gen_Female_count,
        'total_gen_students_count': total_gen_students_count,
        'sc_male_teachers_count': sc_male_teachers_count,
        'sc_female_teachers_count': sc_female_teachers_count,
        'total_sc_teachers_count': total_sc_teachers_count,
        'bca_male_teachers_count': bca_male_teachers_count,
        'bca_female_teachers_count': bca_female_teachers_count,
        'total_bca_teachers_count': total_bca_teachers_count,
        'bcb_male_teachers_count': bcb_male_teachers_count,
        'bcb_female_teachers_count': bcb_female_teachers_count,
        'total_bcb_teachers_count': total_bcb_teachers_count,
        'gen_male_teachers_count': gen_male_teachers_count,
        'gen_female_teachers_count': gen_female_teachers_count,
        'total_gen_teachers_count': total_gen_teachers_count,
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
    
    