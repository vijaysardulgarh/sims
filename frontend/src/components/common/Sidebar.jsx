import React from 'react';
import { NavLink } from 'react-router-dom';

const DashboardSidebar = ({ role }) => {
  
  // Styling active links in Tailwind
  const navClass = ({ isActive }) => 
    `block px-4 py-3 rounded-lg transition-colors ${isActive ? "bg-blue-600 text-white" : "text-gray-300 hover:bg-gray-800 hover:text-white"}`;

  return (
    <aside className="w-64 bg-gray-900 text-white min-h-screen flex flex-col">
      <div className="p-6 text-center border-b border-gray-800">
        <h2 className="text-2xl font-bold text-blue-400">Portal</h2>
        <p className="text-xs text-gray-400 mt-1 capitalize">{role} Dashboard</p>
      </div>

      <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
        
        {/* ================= ADMIN / PRINCIPAL LINKS ================= */}
        {(role === 'admin' || role === 'principal') && (
          <>
            <NavLink to="/dashboard/overview" className={navClass}>📊 School Overview</NavLink>
            <NavLink to="/dashboard/staff" className={navClass}>🧑‍🏫 Staff Management</NavLink>
            <NavLink to="/dashboard/finance" className={navClass}>💰 Financial Ledger</NavLink>
            <NavLink to="/dashboard/infrastructure" className={navClass}>🏢 Infrastructure</NavLink>
          </>
        )}

        {/* ================= TEACHER LINKS ================= */}
        {role === 'teacher' && (
          <>
            <NavLink to="/dashboard/timetable" className={navClass}>📅 My Timetable</NavLink>
            <NavLink to="/dashboard/incharge" className={navClass}>👥 Class Incharge Panel</NavLink>
            <NavLink to="/dashboard/marks" className={navClass}>📝 Enter Marks/Results</NavLink>
            <NavLink to="/dashboard/attendance" className={navClass}>✅ Mark Attendance</NavLink>
          </>
        )}

        {/* ================= STUDENT LINKS ================= */}
        {role === 'student' && (
          <>
            <NavLink to="/dashboard/profile" className={navClass}>👤 Academic Profile</NavLink>
            <NavLink to="/dashboard/fees" className={navClass}>💳 Fee Ledger</NavLink>
            <NavLink to="/dashboard/library" className={navClass}>📚 Library Status</NavLink>
            <NavLink to="/dashboard/performance" className={navClass}>🏅 Performance & Results</NavLink>
          </>
        )}
      </nav>

      <div className="p-4 border-t border-gray-800">
        <button className="w-full px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded transition">
          Logout
        </button>
      </div>
    </aside>
  );
};

export default DashboardSidebar;