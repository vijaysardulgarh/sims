from .school import SchoolAdmin, AffiliationAdmin, MandatoryPublicDisclosureAdmin, InfrastructureAdmin, AboutSchoolAdmin, PrincipalAdmin #, FacilityAdmin
from .user import UserAdmin
from .student import StudentAdmin, StudentAchievementAdmin, ExamDetailAdmin
from .staff import PostTypeAdmin, StaffAdmin, TeacherAttendanceAdmin, TeacherSubjectAssignmentAdmin, ClassInchargeAdmin, SanctionedPostAdmin
from .schoolclass import ClassAdmin, SectionAdmin, StreamAdmin, MediumAdmin, ClassroomAdmin
from .subject import SubjectAdmin, ClassSubjectAdmin
from .timetable import DayAdmin, TimetableSlotAdmin, TimetableAdmin
# from .events import EventAdmin, NewsAdmin, ExtracurricularActivityAdmin
from .finance import FeeStructureAdmin
# from .library import BookAdmin
from .common import FAQAdmin
# from .documents import DocumentAdmin
from .association import AssociationTypeAdmin, AssociationAdmin, AssociationRoleAdmin, StaffAssociationRoleAssignmentAdmin, SMCMemberAdmin #, CommitteeAdmin, CommitteeMemberAdmin, CommitteeMeetingAdmin
