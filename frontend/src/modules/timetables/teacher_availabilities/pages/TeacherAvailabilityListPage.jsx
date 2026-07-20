import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import teacherAvailabilityService from "../services/teacherAvailabilityService";
import api from "../../../../services/api/axios";

const DAYS = [
  { code: "MON", label: "Monday" },
  { code: "TUE", label: "Tuesday" },
  { code: "WED", label: "Wednesday" },
  { code: "THU", label: "Thursday" },
  { code: "FRI", label: "Friday" },
  { code: "SAT", label: "Saturday" },
];

const TeacherAvailabilityListPage = () => {
  const [teachers, setTeachers] = useState([]);
  const [periods, setPeriods] = useState([]);
  const [teacher, setTeacher] = useState("");
  const [matrix, setMatrix] = useState({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadInitialData();
  }, []);

  useEffect(() => {
    if (teacher) {
      loadMatrix();
    }
  }, [teacher]);

  const loadInitialData = async () => {
    try {
      const [teacherRes, periodRes] = await Promise.all([
        teacherAvailabilityService.getTeachers(),
        api.get("/timetables/period-definitions/"),
      ]);

      setTeachers(teacherRes.data.results || teacherRes.data);
      setPeriods(periodRes.data.results || periodRes.data);
    } catch {
      toast.error("Failed to load initial data");
    }
  };

  const loadMatrix = async () => {
    setLoading(true);
    try {
      const response = await teacherAvailabilityService.getBulkMatrix({ teacher });
      setMatrix(response.data || {});
    } catch {
      toast.error("Unable to load availability.");
    } finally {
      setLoading(false);
    }
  };

  const toggleCell = (day, periodId) => {
    setMatrix((prev) => ({
      ...prev,
      [day]: {
        ...prev[day],
        [periodId]: !prev?.[day]?.[periodId],
      },
    }));
  };

  const markAll = (value) => {
    const updated = {};
    DAYS.forEach((day) => {
      updated[day.code] = {};
      periods.forEach((period) => {
        updated[day.code][period.id] = value;
      });
    });
    setMatrix(updated);
  };

  const copyMonday = () => {
    const monday = matrix.MON || {};
    const updated = {};
    DAYS.forEach((day) => {
      updated[day.code] = { ...monday };
    });
    setMatrix(updated);
  };

  const save = async () => {
    try {
      const availability = [];
      DAYS.forEach((day) => {
        periods.forEach((period) => {
          availability.push({
            day: day.code,
            period: period.id,
            is_available: matrix?.[day.code]?.[period.id] ?? true,
          });
        });
      });

      await teacherAvailabilityService.bulkSave({ teacher, availability });
      toast.success("Availability saved successfully.");
    } catch {
      toast.error("Unable to save changes.");
    }
  };

  return (
    <div className="w-full bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
      
      {/* Header Section */}
      <div className="px-6 py-4 border-b border-gray-200 bg-gray-50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-lg font-semibold text-gray-800">Teacher Availability Matrix</h2>
          <p className="text-sm text-gray-500">Manage daily period schedules for staff</p>
        </div>
        <button
          onClick={save}
          disabled={!teacher || loading}
          className="inline-flex items-center justify-center px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm"
        >
          <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
          </svg>
          Save Changes
        </button>
      </div>

      {/* Control Panel Section */}
      <div className="p-6 grid grid-cols-1 lg:grid-cols-3 gap-6 border-b border-gray-100 bg-white">
        
        {/* Teacher Selection */}
        <div className="flex flex-col justify-center space-y-1">
          <label className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
            Teacher
          </label>
          <select
            className="w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-sm py-2 px-3 border"
            value={teacher}
            onChange={(e) => setTeacher(e.target.value)}
          >
            <option value="">Select a Teacher...</option>
            {teachers.map((item) => (
              <option key={item.id} value={item.id}>
                {item.employee_id} - {item.teacher_name}
              </option>
            ))}
          </select>
        </div>

        {/* Legend */}
        <div className="flex flex-col justify-center space-y-2 lg:pl-6 lg:border-l border-gray-200">
          <label className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
            Legend
          </label>
          <div className="flex items-center space-x-6 text-sm text-gray-600">
            <div className="flex items-center">
              <span className="w-3 h-3 rounded-full bg-green-500 mr-2 shadow-sm"></span>
              Available
            </div>
            <div className="flex items-center">
              <span className="w-3 h-3 rounded-full bg-red-500 mr-2 shadow-sm"></span>
              Unavailable
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="flex flex-col justify-center space-y-2 lg:pl-6 lg:border-l border-gray-200">
          <label className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
            Quick Actions
          </label>
          <div className="flex flex-wrap gap-2">
            <button 
              onClick={() => markAll(true)}
              className="px-3 py-1.5 text-xs font-medium text-green-700 bg-green-50 border border-green-200 rounded hover:bg-green-100 transition-colors"
            >
              ✓ All Available
            </button>
            <button 
              onClick={() => markAll(false)}
              className="px-3 py-1.5 text-xs font-medium text-red-700 bg-red-50 border border-red-200 rounded hover:bg-red-100 transition-colors"
            >
              ✕ All Unavailable
            </button>
            <button 
              onClick={copyMonday}
              className="px-3 py-1.5 text-xs font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded hover:bg-gray-100 transition-colors"
            >
              📋 Copy Monday → All
            </button>
          </div>
        </div>

      </div>

      {/* Matrix Table Section */}
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm text-gray-600">
          <thead className="bg-gray-50 border-b border-gray-200 text-gray-700">
            <tr>
              <th className="px-6 py-4 font-semibold w-40">Day / Period</th>
              {periods.map((period) => (
                <th key={period.id} className="px-4 py-4 font-semibold text-center whitespace-nowrap">
                  {period.name}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {DAYS.map((day) => (
              <tr key={day.code} className="hover:bg-gray-50 transition-colors">
                <td className="px-6 py-4 font-medium text-gray-900">
                  {day.label}
                </td>
                {periods.map((period) => {
                  const isAvailable = matrix?.[day.code]?.[period.id] ?? true;
                  return (
                    <td key={period.id} className="px-4 py-3 text-center">
                      <button
                        onClick={() => toggleCell(day.code, period.id)}
                        disabled={!teacher}
                        className={`
                          inline-flex items-center justify-center w-8 h-8 rounded-full transition-all duration-200
                          ${!teacher ? 'opacity-50 cursor-not-allowed' : 'hover:ring-4 cursor-pointer'}
                          ${isAvailable 
                            ? 'bg-green-100 text-green-600 hover:ring-green-50' 
                            : 'bg-red-100 text-red-600 hover:ring-red-50'
                          }
                        `}
                        title={`Toggle ${day.label} ${period.name}`}
                      >
                        <span className={`w-3 h-3 rounded-full shadow-sm ${isAvailable ? 'bg-green-500' : 'bg-red-500'}`}></span>
                      </button>
                    </td>
                  );
                })}
              </tr>
            ))}
            {DAYS.length === 0 && (
              <tr>
                <td colSpan={periods.length + 1} className="px-6 py-8 text-center text-gray-500">
                  No days configured.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      
    </div>
  );
};

export default TeacherAvailabilityListPage;