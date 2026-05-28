// ============================================
// STAFF ROUTES
// File: staffRoutes.jsx
// ============================================

import {
  Routes,
  Route,
} from "react-router-dom";

// ============================================
// DASHBOARD
// ============================================

import StaffDashboard
from "../modules/staff/dashboard/StaffDashboard";

// ============================================
// STAFF
// ============================================

import AddStaff
from "../modules/staff/staff/AddStaff";

import EditStaff
from "../modules/staff/staff/EditStaff";

import StaffList
from "../modules/staff/staff/StaffList";

import StaffProfile
from "../modules/staff/staff/StaffProfile";

// ============================================
// POST TYPES
// ============================================

import AddPostType
from "../modules/staff/post-types/AddPostType";

import EditPostType
from "../modules/staff/post-types/EditPostType";

import PostTypesList
from "../modules/staff/post-types/PostTypesList";

// ============================================
// CLASS INCHARGE
// ============================================

import AddClassIncharge
from "../modules/staff/class-incharge/AddClassIncharge";

import EditClassIncharge
from "../modules/staff/class-incharge/EditClassIncharge";

import ClassInchargeList
from "../modules/staff/class-incharge/ClassInchargeList";

// ============================================
// SANCTIONED POSTS
// ============================================

import AddSanctionedPost
from "../modules/staff/sanctioned-posts/AddSanctionedPost";

import EditSanctionedPost
from "../modules/staff/sanctioned-posts/EditSanctionedPost";

import SanctionedPostsList
from "../modules/staff/sanctioned-posts/SanctionedPostsList";

// ============================================
// TEACHER ATTENDANCE
// ============================================

import AddTeacherAttendance
from "../modules/staff/teacher-attendance/AddTeacherAttendance";

import EditTeacherAttendance
from "../modules/staff/teacher-attendance/EditTeacherAttendance";

import TeacherAttendanceList
from "../modules/staff/teacher-attendance/TeacherAttendanceList";

// ============================================
// TEACHER TIMETABLE
// ============================================

import TeacherTimetable
from "../modules/staff/teacher-timetable/TeacherTimetable";

import TeacherWorkload
from "../modules/staff/teacher-timetable/TeacherWorkload";

import TeacherFreePeriods
from "../modules/staff/teacher-timetable/TeacherFreePeriods";

// ============================================
// REPORTS
// ============================================

import StaffReport
from "../modules/staff/reports/StaffReport";

import AttendanceReport
from "../modules/staff/reports/AttendanceReport";

import VacancyReport
from "../modules/staff/reports/VacancyReport";

import WorkloadReport
from "../modules/staff/reports/WorkloadReport";

// ============================================
// ROUTES
// ============================================

const StaffRoutes = () => {

  return (

    <Routes>

      {/* ================================== */}
      {/* DASHBOARD */}
      {/* ================================== */}

      <Route
        path="dashboard"
        element={<StaffDashboard />}
      />

      {/* ================================== */}
      {/* STAFF */}
      {/* ================================== */}

      <Route
        path="staff"
        element={<StaffList />}
      />

      <Route
        path="staff/add"
        element={<AddStaff />}
      />

      <Route
        path="staff/edit/:id"
        element={<EditStaff />}
      />

      <Route
        path="staff/profile/:id"
        element={<StaffProfile />}
      />

      {/* ================================== */}
      {/* POST TYPES */}
      {/* ================================== */}

      <Route
        path="post-types"
        element={<PostTypesList />}
      />

      <Route
        path="post-types/add"
        element={<AddPostType />}
      />

      <Route
        path="post-types/edit/:id"
        element={<EditPostType />}
      />

      {/* ================================== */}
      {/* CLASS INCHARGE */}
      {/* ================================== */}

      <Route
        path="class-incharge"
        element={<ClassInchargeList />}
      />

      <Route
        path="class-incharge/add"
        element={<AddClassIncharge />}
      />

      <Route
        path="class-incharge/edit/:id"
        element={<EditClassIncharge />}
      />

      {/* ================================== */}
      {/* SANCTIONED POSTS */}
      {/* ================================== */}

      <Route
        path="sanctioned-posts"
        element={<SanctionedPostsList />}
      />

      <Route
        path="sanctioned-posts/add"
        element={<AddSanctionedPost />}
      />

      <Route
        path="sanctioned-posts/edit/:id"
        element={<EditSanctionedPost />}
      />

      {/* ================================== */}
      {/* TEACHER ATTENDANCE */}
      {/* ================================== */}

      <Route
        path="teacher-attendance"
        element={<TeacherAttendanceList />}
      />

      <Route
        path="teacher-attendance/add"
        element={<AddTeacherAttendance />}
      />

      <Route
        path="teacher-attendance/edit/:id"
        element={<EditTeacherAttendance />}
      />

      {/* ================================== */}
      {/* TEACHER TIMETABLE */}
      {/* ================================== */}

      <Route
        path="teacher-timetable/:staffId"
        element={<TeacherTimetable />}
      />

      <Route
        path="teacher-workload/:staffId"
        element={<TeacherWorkload />}
      />

      <Route
        path="teacher-free-periods/:staffId"
        element={<TeacherFreePeriods />}
      />

      {/* ================================== */}
      {/* REPORTS */}
      {/* ================================== */}

      <Route
        path="reports/staff"
        element={<StaffReport />}
      />

      <Route
        path="reports/attendance"
        element={<AttendanceReport />}
      />

      <Route
        path="reports/vacancy"
        element={<VacancyReport />}
      />

      <Route
        path="reports/workload"
        element={<WorkloadReport />}
      />

    </Routes>
  );
};

export default StaffRoutes;