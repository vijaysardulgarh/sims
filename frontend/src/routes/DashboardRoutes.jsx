import { Routes, Route } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

// =========================
// SYSTEM LEVEL
// =========================

import SuperAdminDashboard from "../dashboard/super-admin/Dashboard";
import ClusterAdminDashboard from "../dashboard/cluster-admin/Dashboard";

// =========================
// SCHOOL MANAGEMENT
// =========================

import AdminDashboard from "../dashboard/admin/Dashboard";
import PrincipalDashboard from "../dashboard/principal/Dashboard";
import VicePrincipalDashboard from "../dashboard/vice-principal/Dashboard";

// =========================
// STAFF
// =========================

import TeacherDashboard from "../dashboard/teacher/Dashboard";

import AccountantDashboard from "../dashboard/accountant/Dashboard";
import ClerkDashboard from "../dashboard/clerk/Dashboard";
import ReceptionistDashboard from "../dashboard/receptionist/Dashboard";

// =========================
// SUPPORT & OPERATIONS
// =========================

import LibrarianDashboard from "../dashboard/librarian/Dashboard";
import HostelWardenDashboard from "../dashboard/hostel-warden/Dashboard";
import SecuritySupervisorDashboard from "../dashboard/security-supervisor/Dashboard";

// =========================
// END USERS
// =========================

import StudentDashboard from "../dashboard/student/Dashboard";
import ParentDashboard from "../dashboard/parent/Dashboard";

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

      </Route>

    </Routes>
  );
};

export default DashboardRoutes;