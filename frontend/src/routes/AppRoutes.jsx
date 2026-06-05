// src/routes/AppRoutes.jsx

import {
    Routes,
    Route,
} from "react-router-dom";

import RollCallPrintPage
from "../modules/students/reports/roll-call/pages/RollCallPrintPage";

// =====================================
// WEBSITE
// =====================================

import WebsiteRoutes from "../website/routes/WebsiteRoutes";

// =====================================
// AUTH
// =====================================

import LoginPage from "../modules/accounts/auth/pages/LoginPage";

// =====================================
// DASHBOARD
// =====================================

import DashboardLayout from "../modules/home/layouts/DashboardLayout";
import moduleRoutes from "../modules/moduleRoutes";
import ProtectedRoute from "./ProtectedRoute";

// =====================================
// COMPONENT SHOWCASE
// =====================================

import ComponentShowcasePage from "../pages/ComponentShowcasePage";

// =====================================
// APP ROUTES
// =====================================

const AppRoutes = () => {
    return (
        <Routes>

            {/* ============================= */}
            {/* LOGIN */}
            {/* ============================= */}

            <Route
                path="/login"
                element={<LoginPage />}
            />

            {/* ============================= */}
            {/* COMPONENT SHOWCASE */}
            {/* ============================= */}

            <Route
                path="/component-showcase"
                element={<ComponentShowcasePage />}
            />

            {/* ============================= */}
            {/* DASHBOARD (PROTECTED) */}
            {/* ============================= */}

            <Route
                path="/dashboard/*"
                element={
                    <ProtectedRoute>
                        <DashboardLayout />
                    </ProtectedRoute>
                }
            >
                {moduleRoutes}
            </Route>

            {/* ============================= */}
            {/* PUBLIC WEBSITE */}
            {/* ============================= */}

            <Route
                path="/*"
                element={<WebsiteRoutes />}
            />


            <Route
                path="/print/roll-call"
                element={
                    <ProtectedRoute>
                        <RollCallPrintPage />
                    </ProtectedRoute>
                }
            />

        </Routes>
    );
};

export default AppRoutes;