import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20 items-center">
          
          {/* Logo Section */}
          <div className="flex-shrink-0 flex items-center">
            <Link to="/" className="text-2xl font-bold text-blue-800">
              SIMS
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-6 items-center">
            <Link to="/" className="text-gray-700 hover:text-blue-600 font-medium">Home</Link>
            
            {/* About Us Dropdown */}
            <div className="relative group">
              <button className="text-gray-700 hover:text-blue-600 font-medium flex items-center">
                About Us <span className="ml-1">▼</span>
              </button>
              <div className="absolute left-0 mt-2 w-48 bg-white border border-gray-100 shadow-lg rounded-md hidden group-hover:block">
                <Link to="/about/overview" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Overview</Link>
                <Link to="/about/leadership" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Leadership & Faculty</Link>
                <Link to="/about/disclosure" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Mandatory Disclosure</Link>
              </div>
            </div>

            {/* Academics Dropdown */}
            <div className="relative group">
              <button className="text-gray-700 hover:text-blue-600 font-medium flex items-center">
                Academics <span className="ml-1">▼</span>
              </button>
              <div className="absolute left-0 mt-2 w-48 bg-white border border-gray-100 shadow-lg rounded-md hidden group-hover:block">
                <Link to="/academics/curriculum" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Curriculum</Link>
                <Link to="/academics/structure" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Academic Structure</Link>
                <Link to="/academics/timetable" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Time Table</Link>
              </div>
            </div>

            <Link to="/campus-life" className="text-gray-700 hover:text-blue-600 font-medium">Campus Life</Link>
            <Link to="/contact" className="text-gray-700 hover:text-blue-600 font-medium">Contact</Link>
          </div>

          {/* Right Aligned CTAs */}
          <div className="hidden md:flex space-x-4">
            <Link to="/admissions" className="px-5 py-2 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 transition">
              Apply Now
            </Link>
            <a href="https://your-erp-portal.com" target="_blank" rel="noreferrer" className="px-5 py-2 border-2 border-blue-600 text-blue-600 font-semibold rounded-md hover:bg-blue-50 transition">
              Portal Login
            </a>
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden flex items-center">
            <button onClick={() => setIsOpen(!isOpen)} className="text-gray-700 hover:text-blue-600 focus:outline-none">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16m-7 6h7"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile Menu (simplified for brevity) */}
      {isOpen && (
        <div className="md:hidden bg-gray-50 px-4 pt-2 pb-4 space-y-2">
          <Link to="/" className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:bg-gray-200">Home</Link>
          <Link to="/admissions" className="block px-3 py-2 rounded-md text-base font-medium text-white bg-blue-600 text-center">Apply Now</Link>
        </div>
      )}
    </nav>
  );
};

export default Navbar;