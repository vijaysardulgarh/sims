import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import api from "../../../../services/api/axios";

const ENDPOINT = "/timetables/working-days";

const DEFAULT_DAYS = [
    { id: null, display_order: 1, day_code: "MON", day_name: "Monday", is_working_day: true, is_half_day: false, remarks: "" },
    { id: null, display_order: 2, day_code: "TUE", day_name: "Tuesday", is_working_day: true, is_half_day: false, remarks: "" },
    { id: null, display_order: 3, day_code: "WED", day_name: "Wednesday", is_working_day: true, is_half_day: false, remarks: "" },
    { id: null, display_order: 4, day_code: "THU", day_name: "Thursday", is_working_day: true, is_half_day: false, remarks: "" },
    { id: null, display_order: 5, day_code: "FRI", day_name: "Friday", is_working_day: true, is_half_day: false, remarks: "" },
    { id: null, display_order: 6, day_code: "SAT", day_name: "Saturday", is_working_day: true, is_half_day: true, remarks: "Half Day" },
    { id: null, display_order: 7, day_code: "SUN", day_name: "Sunday", is_working_day: false, is_half_day: false, remarks: "Weekly Off" },
];

export default function WorkingDaysPage() {
    const [rows, setRows] = useState([]);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);

    useEffect(() => {
        fetchWorkingDays();
    }, []);

    const fetchWorkingDays = async () => {
        try {
            const response = await api.get(`${ENDPOINT}/`);
            const fetchedData = response.data.results || response.data || [];
            
            if (fetchedData.length === 0) {
                setRows(DEFAULT_DAYS);
            } else {
                // SMART MERGE: Forces exactly 7 rows and fixes empty database names
                const mergedDays = DEFAULT_DAYS.map(defaultDay => {
                    const savedDay = fetchedData.find(d => d.day_code === defaultDay.day_code);
                    
                    if (savedDay) {
                        return {
                            ...defaultDay,
                            ...savedDay,
                            // Ensure names aren't overwritten by blank database entries
                            day_name: savedDay.day_name || defaultDay.day_name,
                            day_code: savedDay.day_code || defaultDay.day_code
                        };
                    }
                    return defaultDay;
                });
                
                setRows(mergedDays);
            }
        } catch (error) {
            console.error(error);
            toast.error("Failed to load working days.");
            setRows(DEFAULT_DAYS);
        } finally {
            setLoading(false);
        }
    };

    const updateRow = (index, field, value) => {
        const updated = [...rows];
        updated[index][field] = value;

        if (field === "is_working_day" && value === false) {
            updated[index].is_half_day = false;
        }
        setRows(updated);
    };

    const resetDefaults = () => {
        setRows(JSON.parse(JSON.stringify(DEFAULT_DAYS)));
        toast.success("Reset to defaults. Don't forget to save changes.");
    };

    const save = async () => {
        try {
            setSaving(true);
            await api.post(`${ENDPOINT}/save/`, rows);
            toast.success("Working days saved successfully.");
            fetchWorkingDays();
        } catch (error) {
            console.error(error);
            toast.error("Unable to save working days.");
        } finally {
            setSaving(false);
        }
    };

    const workingDaysCount = rows.filter((r) => r.is_working_day).length;

    if (loading) {
        return (
            <div className="flex h-64 items-center justify-center p-6">
                <div className="h-8 w-8 animate-spin rounded-full border-4 border-blue-600 border-t-transparent"></div>
            </div>
        );
    }

    return (
        <div className="mx-auto max-w-5xl p-6">
            <div className="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
                
                {/* Header Section */}
                <div className="border-b border-gray-200 bg-gray-50/50 p-6">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-blue-100 text-blue-600">
                                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                </svg>
                            </div>
                            <div>
                                <h1 className="text-xl font-bold text-gray-900">Working Days</h1>
                                <p className="text-sm text-gray-500">Configure weekly working days for this academic session</p>
                            </div>
                        </div>
                        <div className="rounded-full bg-blue-50 px-4 py-1.5 text-sm font-medium text-blue-700">
                            {workingDaysCount} Working Days
                        </div>
                    </div>
                </div>

                {/* Table Section */}
                <div className="overflow-x-auto">
                    <table className="min-w-full text-left text-sm text-gray-700">
                        <thead className="bg-white text-gray-500 border-b border-gray-200">
                            <tr>
                                <th className="px-6 py-4 font-semibold w-24">Order</th>
                                <th className="px-6 py-4 font-semibold">Day</th>
                                <th className="px-6 py-4 font-semibold text-center w-32">Working</th>
                                <th className="px-6 py-4 font-semibold text-center w-32">Half Day</th>
                                <th className="px-6 py-4 font-semibold">Remarks</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-100">
                            {rows.map((row, index) => (
                                <tr key={row.day_code || index} className="transition-colors hover:bg-gray-50">
                                    
                                    {/* Order */}
                                    <td className="px-6 py-3">
                                        <input
                                            type="number"
                                            className="w-16 rounded-md border border-gray-300 bg-white px-3 py-1.5 text-center text-sm transition-all focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                                            value={row.display_order}
                                            onChange={(e) => updateRow(index, "display_order", Number(e.target.value))}
                                        />
                                    </td>

                                    {/* Day Name */}
                                    <td className="px-6 py-3 font-medium text-gray-900">
                                        <div className="flex items-center gap-2">
                                            <span className="text-blue-500">
                                                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                                    <path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd" />
                                                </svg>
                                            </span>
                                            {row.day_name}
                                        </div>
                                    </td>

                                    {/* Working Toggle */}
                                    <td className="px-6 py-3 text-center">
                                        <button
                                            onClick={() => updateRow(index, "is_working_day", !row.is_working_day)}
                                            className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 ${row.is_working_day ? 'bg-blue-600' : 'bg-gray-300'}`}
                                        >
                                            <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${row.is_working_day ? 'translate-x-6' : 'translate-x-1'}`} />
                                        </button>
                                        <span className="ml-2 inline-block w-8 text-xs font-semibold text-gray-500">
                                            {row.is_working_day ? 'ON' : 'OFF'}
                                        </span>
                                    </td>

                                    {/* Half Day Toggle */}
                                    <td className="px-6 py-3 text-center">
                                        {row.is_working_day ? (
                                            <>
                                                <button
                                                    onClick={() => updateRow(index, "is_half_day", !row.is_half_day)}
                                                    className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 ${row.is_half_day ? 'bg-indigo-500' : 'bg-gray-300'}`}
                                                >
                                                    <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${row.is_half_day ? 'translate-x-6' : 'translate-x-1'}`} />
                                                </button>
                                                <span className="ml-2 inline-block w-8 text-xs font-semibold text-gray-500">
                                                    {row.is_half_day ? 'ON' : 'OFF'}
                                                </span>
                                            </>
                                        ) : (
                                            <span className="text-xs font-medium text-gray-400 bg-gray-100 px-2 py-1 rounded">Disabled</span>
                                        )}
                                    </td>

                                    {/* Remarks */}
                                    <td className="px-6 py-3">
                                        <input
                                            type="text"
                                            placeholder="Add remarks..."
                                            className="w-full rounded-md border border-transparent bg-transparent px-3 py-1.5 text-sm transition-all hover:border-gray-300 focus:border-blue-500 focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500"
                                            value={row.remarks || ""}
                                            onChange={(e) => updateRow(index, "remarks", e.target.value)}
                                        />
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                {/* Footer Actions */}
                <div className="flex items-center justify-end gap-4 border-t border-gray-200 bg-gray-50/50 px-6 py-4">
                    <button
                        onClick={resetDefaults}
                        disabled={saving}
                        className="rounded-lg px-5 py-2.5 text-sm font-medium text-gray-700 transition-colors hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-300 focus:ring-offset-2 disabled:opacity-50"
                    >
                        Reset Defaults
                    </button>
                    <button
                        onClick={save}
                        disabled={saving}
                        className="flex items-center gap-2 rounded-lg bg-blue-600 px-6 py-2.5 text-sm font-medium text-white shadow-sm transition-colors hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50"
                    >
                        {saving ? (
                            <>
                                <svg className="h-4 w-4 animate-spin text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                                Saving...
                            </>
                        ) : (
                            "Save Changes"
                        )}
                    </button>
                </div>
            </div>
        </div>
    );
}