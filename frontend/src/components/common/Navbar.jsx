import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 bg-white shadow-md">

      <div className="max-w-7xl mx-auto px-4">

        <div className="flex items-center justify-between h-20">

          {/* Logo */}
          <Link to="/" className="flex items-center gap-3">

            <div className="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center text-white text-2xl font-bold">
              S
            </div>

            <div>

              <h1 className="text-2xl font-bold text-gray-800">
                SIMS
              </h1>

              <p className="text-xs text-gray-500">
                School Information Management System
              </p>

            </div>

          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center gap-8">

            {/* Home */}
            <Link
              to="/"
              className="font-medium text-gray-700 hover:text-blue-600 transition"
            >
              Home
            </Link>

            {/* About Dropdown */}
            <div className="relative group">

              <button className="font-medium text-gray-700 hover:text-blue-600 transition">
                About Us
              </button>

              <div className="absolute left-0 top-full pt-2 hidden group-hover:block">

                <div className="bg-white shadow-xl rounded-xl w-72 p-4 border border-gray-100">

                  <div className="space-y-3">

                    <Link
                      to="/about/overview"
                      className="block hover:text-blue-600 transition"
                    >
                      Overview
                    </Link>

                    <Link
                      to="/about/leadership"
                      className="block hover:text-blue-600 transition"
                    >
                      Leadership & Faculty
                    </Link>

                    <Link
                      to="/about/mandatory-disclosure"
                      className="block hover:text-blue-600 transition"
                    >
                      Mandatory Disclosure
                    </Link>

                  </div>

                </div>

              </div>

            </div>

            {/* Academics Dropdown */}
            <div className="relative group">

              <button className="font-medium text-gray-700 hover:text-blue-600 transition">
                Academics
              </button>

              <div className="absolute left-0 top-full pt-2 hidden group-hover:block">

                <div className="bg-white shadow-xl rounded-xl w-72 p-4 border border-gray-100">

                  <div className="space-y-3">

                    <Link
                      to="/academics/curriculum"
                      className="block hover:text-blue-600 transition"
                    >
                      Curriculum & Syllabus
                    </Link>

                    <Link
                      to="/academics/academic-structure"
                      className="block hover:text-blue-600 transition"
                    >
                      Academic Structure
                    </Link>

                    <Link
                      to="/academics/timetable"
                      className="block hover:text-blue-600 transition"
                    >
                      Timetable & Schedules
                    </Link>

                  </div>

                </div>

              </div>

            </div>

            {/* Campus Life */}
            <Link
              to="/campus-life"
              className="font-medium text-gray-700 hover:text-blue-600 transition"
            >
              Campus Life
            </Link>

            {/* Updates Dropdown */}
            <div className="relative group">

              <button className="font-medium text-gray-700 hover:text-blue-600 transition">
                Updates & Resources
              </button>

              <div className="absolute left-0 top-full pt-2 hidden group-hover:block">

                <div className="bg-white shadow-xl rounded-xl w-72 p-4 border border-gray-100">

                  <div className="space-y-3">

                    <Link
                      to="/updates/news-events"
                      className="block hover:text-blue-600 transition"
                    >
                      News & Events
                    </Link>

                    <Link
                      to="/updates/downloads"
                      className="block hover:text-blue-600 transition"
                    >
                      Downloads
                    </Link>

                  </div>

                </div>

              </div>

            </div>

            {/* Contact */}
            <Link
              to="/contact"
              className="font-medium text-gray-700 hover:text-blue-600 transition"
            >
              Contact Us
            </Link>

          </nav>

          {/* Right Buttons */}
          <div className="hidden lg:flex items-center gap-4">

            <Link
              to="/admissions"
              className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl font-medium transition"
            >
              Apply Now
            </Link>

            <Link
              to="/login"
              className="border border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white px-5 py-3 rounded-xl font-medium transition"
            >
              Portal Login
            </Link>

          </div>

          {/* Mobile Button */}
          <button className="lg:hidden text-3xl text-gray-700">
            ☰
          </button>

        </div>

      </div>

    </header>
  );
}