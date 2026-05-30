import {
  Routes,
  Route,
  Navigate
} from "react-router-dom";


// =====================================
// WEBSITE
// =====================================

import WebsiteRoutes
from "../website/routes/WebsiteRoutes";


// =====================================
// AUTH
// =====================================

import LoginPage from "../modules/accounts/auth/pages/LoginPage";


// =====================================
// DASHBOARD
// =====================================

import DashboardLayout
from "../modules/home/layouts/DashboardLayout";

import moduleRoutes
from "../modules/moduleRoutes";

import ProtectedRoute
from "./ProtectedRoute";


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
          {/* DASHBOARD */}
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
          {/* WEBSITE */}
          {/* ============================= */}

          <Route

              path="/*"

              element={<WebsiteRoutes />}
          />


          {/* ============================= */}
          {/* FALLBACK */}
          {/* ============================= */}

          <Route

              path="*"

              element={
                  <Navigate
                      to="/login"
                      replace
                  />
              }
          />

      </Routes>
  );
};


export default AppRoutes;