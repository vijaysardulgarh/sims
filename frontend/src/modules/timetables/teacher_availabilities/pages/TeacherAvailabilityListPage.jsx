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
  { code: "SUN", label: "Sunday" },
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
      
      const apiData = response.data || [];
      if (Array.isArray(apiData)) {
        const formattedMatrix = {};
        apiData.forEach((item) => {
          if (!formattedMatrix[item.day]) formattedMatrix[item.day] = {};
          formattedMatrix[item.day][item.period] = item.is_available;
        });
        setMatrix(formattedMatrix);
      } else {
        setMatrix(apiData);
      }
    } catch {
      toast.error("Unable to load availability.");
    } finally {
      setLoading(false);
    }
  };

  const toggleCell = (dayCode, periodId) => {
    setMatrix((prev) => {
      const dayData = prev[dayCode] || {};
      const isCurrentlyAvailable = dayData[periodId] ?? true;
      return {
        ...prev,
        [dayCode]: {
          ...dayData,
          [periodId]: !isCurrentlyAvailable,
        },
      };
    });
  };

  const togglePeriodColumn = (periodId) => {
    if (!teacher) return;
    setMatrix((prev) => {
      const allAvailable = DAYS.every((day) => prev?.[day.code]?.[periodId] ?? true);
      const newValue = !allAvailable;
      
      const nextMatrix = { ...prev };
      DAYS.forEach((day) => {
        nextMatrix[day.code] = {
          ...(nextMatrix[day.code] || {}),
          [periodId]: newValue,
        };
      });
      return nextMatrix;
    });
  };

  const toggleDayRow = (dayCode) => {
    if (!teacher) return;
    setMatrix((prev) => {
      const allAvailable = periods.every((p) => prev?.[dayCode]?.[p.id] ?? true);
      const newValue = !allAvailable;
      
      const nextMatrix = { ...prev };
      nextMatrix[dayCode] = { ...(nextMatrix[dayCode] || {}) };
      periods.forEach((p) => {
        nextMatrix[dayCode][p.id] = newValue;
      });
      return nextMatrix;
    });
  };

  const markAll = (isAvailable) => {
    const updated = {};
    DAYS.forEach((day) => {
      updated[day.code] = {};
      periods.forEach((period) => {
        updated[day.code][period.id] = isAvailable;
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
    <div className="w-full bg-white rounded-xl shadow-md border border-slate-200 overflow-hidden flex flex-col">
      
      {/* Header Section */}
      <div className="px-6 py-5 border-b border-slate-200 bg-slate-50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-800">Teacher Availability Matrix</h2>
          <p className="text-sm text-slate-500 mt-1">Configure weekly period schedules and off-times for staff</p>
        </div>
        <button
          onClick={save}
          disabled={!teacher || loading}
          className="inline-flex items-center justify-center px-5 py-2.5 bg-blue-600 text-white text-sm font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-sm focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
        >
          {loading ? (
            <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          ) : (
            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
            </svg>
          )}
          Save Changes
        </button>
      </div>

      {/* Control Panel Section */}
      <div className="p-6 grid grid-cols-1 lg:grid-cols-12 gap-6 border-b border-slate-200 bg-white items-end">
        
        {/* Teacher Selection */}
        <div className="lg:col-span-4 flex flex-col space-y-2">
          <label className="text-xs font-bold text-slate-500 uppercase tracking-wider">
            Select Teacher
          </label>
          <select
            className="w-full border-slate-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-sm py-2.5 px-3 border bg-slate-50"
            value={teacher}
            onChange={(e) => setTeacher(e.target.value)}
          >
            <option value="">-- Choose a teacher --</option>
            {teachers.map((item) => (
              <option key={item.id} value={item.id}>
                {item.employee_id} - {item.teacher_name}
              </option>
            ))}
          </select>
        </div>

        {/* Legend */}
        <div className="lg:col-span-3 flex flex-col space-y-2">
          <label className="text-xs font-bold text-slate-500 uppercase tracking-wider hidden lg:block">
            Legend
          </label>
          <div className="flex items-center space-x-4 text-sm font-medium text-slate-600 h-[42px]">
            <div className="flex items-center">
              <div className="w-4 h-4 rounded bg-emerald-100 border border-emerald-300 mr-2 flex items-center justify-center">
                <svg className="w-3 h-3 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              Available
            </div>
            <div className="flex items-center">
              <div className="w-4 h-4 rounded bg-rose-50 border border-rose-200 mr-2 flex items-center justify-center">
                <svg className="w-3 h-3 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M6 18L18 6M6 6l12 12"></path></svg>
              </div>
              Unavailable
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="lg:col-span-5 flex flex-col space-y-2 lg:items-end">
          <label className="text-xs font-bold text-slate-500 uppercase tracking-wider hidden lg:block">
            Quick Actions
          </label>
          <div className="flex flex-wrap gap-2 h-[42px] items-center">
            <button 
              onClick={() => markAll(true)}
              disabled={!teacher}
              className="px-3 py-2 text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded-md hover:bg-emerald-100 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
            >
              <svg className="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M5 13l4 4L19 7"></path></svg>
              All Available
            </button>
            <button 
              onClick={() => markAll(false)}
              disabled={!teacher}
              className="px-3 py-2 text-xs font-semibold text-rose-700 bg-rose-50 border border-rose-200 rounded-md hover:bg-rose-100 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
            >
              <svg className="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M6 18L18 6M6 6l12 12"></path></svg>
              All Unavailable
            </button>
            <button 
              onClick={copyMonday}
              disabled={!teacher}
              className="px-3 py-2 text-xs font-semibold text-slate-700 bg-slate-100 border border-slate-200 rounded-md hover:bg-slate-200 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
            >
              <svg className="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
              Copy Mon → All
            </button>
          </div>
        </div>

      </div>

      {/* Matrix Table Section */}
      <div className="overflow-x-auto bg-slate-50 p-4 sm:p-6">
        
        {!teacher ? (
          <div className="text-center py-12 bg-white rounded-lg border border-dashed border-slate-300">
            <svg className="mx-auto h-12 w-12 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path vectorEffect="non-scaling-stroke" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
            <h3 className="mt-2 text-sm font-semibold text-slate-900">No Teacher Selected</h3>
            <p className="mt-1 text-sm text-slate-500">Select a teacher from the dropdown above to view and edit their schedule.</p>
          </div>
        ) : periods.length === 0 ? (
          <div className="text-center py-12 bg-white rounded-lg border border-dashed border-slate-300">
            <p className="text-sm text-slate-500">No periods found. Please ensure period definitions are set up.</p>
          </div>
        ) : (
          <div className="inline-block min-w-full align-middle">
            <div className="border border-slate-200 rounded-lg overflow-hidden bg-white shadow-sm">
              <table className="min-w-full divide-y divide-slate-200 select-none">
                <thead className="bg-slate-100">
                  <tr>
                    <th className="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider w-40 border-r border-slate-200">
                      Day / Period
                    </th>
                    {periods.map((period) => (
                      <th 
                        key={period.id} 
                        onClick={() => togglePeriodColumn(period.id)}
                        title={`Click to toggle ${period.name} for all days`}
                        className="px-4 py-4 text-center text-xs font-bold text-slate-700 uppercase tracking-wider border-r border-slate-200 cursor-pointer hover:bg-blue-50 hover:text-blue-700 transition-colors group"
                      >
                        <div className="flex flex-col items-center justify-center space-y-1">
                          <span>{period.name}</span>
                          <span className="text-[10px] text-slate-400 font-normal group-hover:text-blue-400">Toggle Col</span>
                        </div>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-slate-200">
                  {DAYS.map((day) => (
                    <tr key={day.code} className="hover:bg-slate-50 transition-colors">
                      <td 
                        onClick={() => toggleDayRow(day.code)}
                        title={`Click to toggle all periods for ${day.label}`}
                        className="px-6 py-4 whitespace-nowrap text-sm font-bold text-slate-700 border-r border-slate-200 cursor-pointer hover:bg-blue-50 hover:text-blue-700 transition-colors group"
                      >
                         <div className="flex items-center justify-between">
                            <span>{day.label}</span>
                            <span className="text-[10px] text-slate-400 font-normal opacity-0 group-hover:opacity-100 transition-opacity group-hover:text-blue-400">Toggle Row</span>
                         </div>
                      </td>
                      {periods.map((period) => {
                        const isAvailable = matrix?.[day.code]?.[period.id] ?? true;
                        return (
                          <td key={period.id} className="p-1.5 border-r border-slate-200 relative group">
                            <button
                              onClick={() => toggleCell(day.code, period.id)}
                              className={`
                                w-full h-12 rounded-md flex items-center justify-center transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-1
                                ${isAvailable 
                                  ? 'bg-emerald-50 text-emerald-600 hover:bg-emerald-100 focus:ring-emerald-500' 
                                  : 'bg-rose-50 text-rose-500 hover:bg-rose-100 focus:ring-rose-400'
                                }
                              `}
                              title={`${isAvailable ? 'Available' : 'Unavailable'} on ${day.label} ${period.name}`}
                            >
                              {isAvailable ? (
                                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                              ) : (
                                <svg className="w-5 h-5 opacity-70" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M6 18L18 6M6 6l12 12"></path>
                                </svg>
                              )}
                            </button>
                          </td>
                        );
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default TeacherAvailabilityListPage;