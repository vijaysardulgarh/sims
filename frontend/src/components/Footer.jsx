import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white pt-12 pb-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          
          {/* Brand Info */}
          <div>
            <h3 className="text-2xl font-bold text-blue-400 mb-4">SIMS</h3>
            <p className="text-gray-400 text-sm">
              Empowering students with modern education, robust infrastructure, and strong core values.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2 text-sm text-gray-400">
              <li><Link to="/about/overview" className="hover:text-blue-400 transition">About Us</Link></li>
              <li><Link to="/academics/curriculum" className="hover:text-blue-400 transition">Academics</Link></li>
              <li><Link to="/campus-life" className="hover:text-blue-400 transition">Campus Life</Link></li>
              <li><Link to="/admissions" className="hover:text-blue-400 transition">Admissions</Link></li>
            </ul>
          </div>

          {/* Resources */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Resources</h4>
            <ul className="space-y-2 text-sm text-gray-400">
              <li><Link to="/updates/news" className="hover:text-blue-400 transition">News & Events</Link></li>
              <li><Link to="/updates/downloads" className="hover:text-blue-400 transition">Downloads & Forms</Link></li>
              <li><Link to="/about/disclosure" className="hover:text-blue-400 transition">Mandatory Disclosure</Link></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="text-lg font-semibold mb-4">Contact Us</h4>
            <ul className="space-y-2 text-sm text-gray-400">
              <li>📍 123 Education Lane, City, State</li>
              <li>📞 +1 (555) 123-4567</li>
              <li>✉️ info@sims.edu</li>
            </ul>
          </div>

        </div>
        <div className="border-t border-gray-800 mt-12 pt-8 text-center text-sm text-gray-500">
          © {new Date().getFullYear()} School Information Management System. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;