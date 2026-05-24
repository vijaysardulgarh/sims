import { Routes, Route } from "react-router-dom";

import WebsiteLayout from "../layouts/WebsiteLayout";

// Home
import Home from "../pages/Home";

// About
import Overview from "../pages/about/Overview";
import Leadership from "../pages/about/Leadership";
import MandatoryDisclosure from "../pages/about/MandatoryDisclosure";

// Academics
import Curriculum from "../pages/academics/Curriculum";
import AcademicStructure from "../pages/academics/AcademicStructure";
import Timetable from "../pages/academics/Timetable";

// Updates
import NewsEvents from "../pages/updates/NewsEvents";
import Downloads from "../pages/updates/Downloads";

// Other Pages
import CampusLife from "../pages/CampusLife";
import Admissions from "../pages/Admissions";
import Contact from "../pages/Contact";

// Auth

import LoginPage from "../../dashboard/modules/accounts/auth/pages/LoginPage";

import ForgotPassword from "../../dashboard/modules/accounts/auth/pages/ForgotPasswordPage";

import ResetPassword from "../../dashboard/modules/accounts/auth/pages/ResetPasswordPage";


export default function WebsiteRoutes() {
  return (
    <Routes>

      {/* Home */}
      <Route
        path="/"
        element={
          <WebsiteLayout>
            <Home />
          </WebsiteLayout>
        }
      />

      {/* About */}
      <Route
        path="/about/overview"
        element={
          <WebsiteLayout>
            <Overview />
          </WebsiteLayout>
        }
      />

      <Route
        path="/about/leadership"
        element={
          <WebsiteLayout>
            <Leadership />
          </WebsiteLayout>
        }
      />

      <Route
        path="/about/mandatory-disclosure"
        element={
          <WebsiteLayout>
            <MandatoryDisclosure />
          </WebsiteLayout>
        }
      />

      {/* Academics */}
      <Route
        path="/academics/curriculum"
        element={
          <WebsiteLayout>
            <Curriculum />
          </WebsiteLayout>
        }
      />

      <Route
        path="/academics/academic-structure"
        element={
          <WebsiteLayout>
            <AcademicStructure />
          </WebsiteLayout>
        }
      />

      <Route
        path="/academics/timetable"
        element={
          <WebsiteLayout>
            <Timetable />
          </WebsiteLayout>
        }
      />

      {/* Updates */}
      <Route
        path="/updates/news-events"
        element={
          <WebsiteLayout>
            <NewsEvents />
          </WebsiteLayout>
        }
      />

      <Route
        path="/updates/downloads"
        element={
          <WebsiteLayout>
            <Downloads />
          </WebsiteLayout>
        }
      />

      {/* Campus Life */}
      <Route
        path="/campus-life"
        element={
          <WebsiteLayout>
            <CampusLife />
          </WebsiteLayout>
        }
      />

      {/* Admissions */}
      <Route
        path="/admissions"
        element={
          <WebsiteLayout>
            <Admissions />
          </WebsiteLayout>
        }
      />

      {/* Contact */}
      <Route
        path="/contact"
        element={
          <WebsiteLayout>
            <Contact />
          </WebsiteLayout>
        }
      />

      {/* Login */}
      <Route
        path="/login"
        element={
          <WebsiteLayout>
            <LoginPage />
          </WebsiteLayout>
        }
      />

            {/* Forgot Password */}
            <Route
        path="/forgot-password"
        element={
          <ForgotPassword />
        }
      />

      {/* Reset Password */}
      <Route
        path="/reset-password"
        element={
          <ResetPassword />
        }
      />

    </Routes>
  );
}