import { Routes, Route } from "react-router-dom";

import WebsiteLayout from "../layouts/WebsiteLayout";

// Home
import Home from "../Home";

// About
import Overview from "../about/Overview";
import Leadership from "../about/Leadership";
import MandatoryDisclosure from "../about/MandatoryDisclosure";

// Academics
import Curriculum from "../academics/Curriculum";
import AcademicStructure from "../academics/AcademicStructure";
import Timetable from "../academics/Timetable";

// Updates
import NewsEvents from "../updates/NewsEvents";
import Downloads from "../updates/Downloads";

// Other Pages
import CampusLife from "../CampusLife";
import Admissions from "../Admissions";
import Contact from "../Contact";

// Auth
import Login from "../../dashboard/auth/Login";
import ForgotPassword from "../../dashboard/auth/ForgotPassword";
import ResetPassword from "../../dashboard/auth/ResetPassword";

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
            <Login />
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