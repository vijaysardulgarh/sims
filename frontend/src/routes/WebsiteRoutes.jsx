import { Routes, Route } from "react-router-dom";

import WebsiteLayout from "../layouts/WebsiteLayout";

// Home
import Home from "../pages/website/Home";

// About
import Overview from "../pages/website/about/Overview";
import Leadership from "../pages/website/about/Leadership";
import MandatoryDisclosure from "../pages/website/about/MandatoryDisclosure";

// Academics
import Curriculum from "../pages/website/academics/Curriculum";
import AcademicStructure from "../pages/website/academics/AcademicStructure";
import Timetable from "../pages/website/academics/Timetable";

// Updates
import NewsEvents from "../pages/website/updates/NewsEvents";
import Downloads from "../pages/website/updates/Downloads";

// Other Pages
import CampusLife from "../pages/website/CampusLife";
import Admissions from "../pages/website/Admissions";
import Contact from "../pages/website/Contact";

// Auth
import Login from "../pages/auth/Login";

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

    </Routes>
  );
}