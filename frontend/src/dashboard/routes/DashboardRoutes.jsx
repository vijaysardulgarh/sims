import { Routes, Route } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

// =========================
// SYSTEM LEVEL
// =========================

import SuperAdminDashboard from "../roles/super-admin/Dashboard";
import ClusterAdminDashboard from "../roles/cluster-admin/Dashboard";

// =========================
// SCHOOL MANAGEMENT
// =========================

import AdminDashboard from "../roles/admin/Dashboard";
import PrincipalDashboard from "../roles/principal/Dashboard";
import VicePrincipalDashboard from "../roles/vice-principal/Dashboard";

// =========================
// STAFF
// =========================

import TeacherDashboard from "../roles/teacher/Dashboard";

import AccountantDashboard from "../roles/accountant/Dashboard";
import ClerkDashboard from "../roles/clerk/Dashboard";
import ReceptionistDashboard from "../roles/receptionist/Dashboard";

// =========================
// SUPPORT & OPERATIONS
// =========================

import LibrarianDashboard from "../roles/librarian/Dashboard";
import HostelWardenDashboard from "../roles/hostel-warden/Dashboard";
import SecuritySupervisorDashboard from "../roles/security-supervisor/Dashboard";

// =========================
// END USERS
// =========================

import StudentDashboard from "../roles/student/Dashboard";
import ParentDashboard from "../roles/parent/Dashboard";



// =========================
// Module LEVEL
// =========================
import StudentsList from "../modules/students/StudentsList";
import AddStudent from "../modules/students/AddStudent";
import EditStudent from "../modules/students/EditStudent";
import StudentProfile from "../modules/students/StudentProfile";

import ClassesList from "../modules/academics/classes/ClassesList";

import AddClass from "../modules/academics/classes/AddClass";

import EditClass from "../modules/academics/classes/EditClass";

const DashboardRoutes = () => {
  return (
    <Routes>

      {/* =========================
          COMMON DASHBOARD LAYOUT
      ========================= */}

      <Route
        path="/dashboard"
        element={<DashboardLayout />}
      >

        {/* =========================
            SYSTEM LEVEL
        ========================= */}

        <Route
          path="super-admin"
          element={<SuperAdminDashboard />}
        />

        <Route
          path="cluster-admin"
          element={<ClusterAdminDashboard />}
        />

        {/* =========================
            SCHOOL MANAGEMENT
        ========================= */}

        <Route
          path="admin"
          element={<AdminDashboard />}
        />

        <Route
          path="principal"
          element={<PrincipalDashboard />}
        />

        <Route
          path="vice-principal"
          element={<VicePrincipalDashboard />}
        />

        {/* =========================
            STAFF
        ========================= */}

        <Route
          path="teacher"
          element={<TeacherDashboard />}
        />

        <Route
          path="accountant"
          element={<AccountantDashboard />}
        />

        <Route
          path="clerk"
          element={<ClerkDashboard />}
        />

        <Route
          path="receptionist"
          element={<ReceptionistDashboard />}
        />

        {/* =========================
            SUPPORT & OPERATIONS
        ========================= */}

        <Route
          path="librarian"
          element={<LibrarianDashboard />}
        />

        <Route
          path="hostel-warden"
          element={<HostelWardenDashboard />}
        />

        <Route
          path="security-supervisor"
          element={<SecuritySupervisorDashboard />}
        />

        {/* =========================
            END USERS
        ========================= */}

        <Route
          path="student"
          element={<StudentDashboard />}
        />

        <Route
          path="parent"
          element={<ParentDashboard />}
        />

        {/* =========================
            Module
        ========================= */}


        <Route
          path="students"
          element={<StudentsList />}
        />
        <Route
          path="students/add"
          element={<AddStudent />}
        />
        <Route
          path="students/edit/:id"
          element={<EditStudent />}
        />
        <Route
          path="students/profile/:id"
          element={<StudentProfile />}
        />        

        <Route
          path="/dashboard/academics/classes"
          element={<ClassesList />}
        />

        <Route
          path="/dashboard/academics/classes/add"
          element={<AddClass />}
        />

        <Route
          path="/dashboard/academics/classes/edit/:id"
          element={<EditClass />}
        />

      </Route>

    </Routes>
  );
};

export default DashboardRoutes;