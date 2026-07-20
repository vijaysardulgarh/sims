import {
    useEffect,
    useMemo,
    useState,
} from "react";

import toast from "react-hot-toast";
import { Save, Search, Users } from "lucide-react";

import teacherWorkloadService from "../services/teacherWorkloadService";

const TeacherWorkloadListPage = () => {

    const [workloads, setWorkloads] = useState([]);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [search, setSearch] = useState("");

    useEffect(() => {

        loadData();

    }, []);

    const loadData = async () => {

        try {

            const response =
                await teacherWorkloadService.getAll();

            setWorkloads(response.data);

        } catch {

            toast.error(
                "Failed to load teacher workloads."
            );

        } finally {

            setLoading(false);

        }

    };

    const handleChange = (
        index,
        field,
        value
    ) => {

        const updated = [...workloads];

        updated[index][field] = Number(value);

        setWorkloads(updated);

    };

    const handleSave = async () => {

        try {

            setSaving(true);

            await teacherWorkloadService.saveAll(
                workloads
            );

            toast.success(
                "Teacher workloads saved successfully."
            );

        } catch (error) {

            console.error(error);

            toast.error(
                error.response?.data?.message ||
                "Failed to save workloads."
            );

        } finally {

            setSaving(false);

        }

    };

    const filteredRows = useMemo(() => {

        return workloads.filter(
            (row) =>
                row.teacher_name
                    ?.toLowerCase()
                    .includes(search.toLowerCase()) ||

                row.employee_id
                    ?.toLowerCase()
                    .includes(search.toLowerCase())
        );

    }, [search, workloads]);

    const averageWeek = workloads.length
        ? Math.round(
            workloads.reduce(
                (sum, item) =>
                    sum + item.max_periods_per_week,
                0
            ) / workloads.length
        )
        : 0;

    if (loading) {

        return (

            <div className="flex justify-center items-center h-80">

                <div className="text-gray-500 text-lg">
                    Loading...
                </div>

            </div>

        );

    }

    return (

        <div className="space-y-6 p-6 bg-gray-50 min-h-screen">

            {/* Header */}

            <div className="bg-white rounded-xl shadow border">

                <div className="flex items-center justify-between p-6">

                    <div>

                        <h1 className="text-2xl font-bold text-gray-800">

                            Teacher Workload Settings

                        </h1>

                        <p className="text-gray-500 mt-1">

                            Configure workload limits used during
                            automatic timetable generation.

                        </p>

                    </div>

                    <button

                        onClick={handleSave}

                        disabled={saving}

                        className="flex items-center gap-2 rounded-lg bg-blue-600 px-5 py-3 text-white font-medium hover:bg-blue-700 transition disabled:opacity-50"

                    >

                        <Save size={18} />

                        {saving
                            ? "Saving..."
                            : "Save All Changes"}

                    </button>

                </div>

            </div>

            {/* Summary */}

            <div className="grid grid-cols-1 md:grid-cols-3 gap-5">

                <div className="bg-white rounded-xl shadow border p-5">

                    <div className="text-gray-500 text-sm">

                        Total Teachers

                    </div>

                    <div className="flex items-center gap-3 mt-2">

                        <Users
                            size={28}
                            className="text-blue-600"
                        />

                        <span className="text-3xl font-bold">

                            {workloads.length}

                        </span>

                    </div>

                </div>

                <div className="bg-white rounded-xl shadow border p-5">

                    <div className="text-gray-500 text-sm">

                        Average Max/Week

                    </div>

                    <div className="text-3xl font-bold mt-2">

                        {averageWeek}

                    </div>

                </div>

                <div className="bg-white rounded-xl shadow border p-5">

                    <div className="text-gray-500 text-sm">

                        Default Max/Day

                    </div>

                    <div className="text-3xl font-bold mt-2">

                        6

                    </div>

                </div>

            </div>

            {/* Search */}

            <div className="bg-white rounded-xl shadow border p-4 flex items-center justify-between">

                <div className="relative w-full max-w-md">

                    <Search
                        className="absolute left-3 top-3 text-gray-400"
                        size={18}
                    />

                    <input

                        type="text"

                        placeholder="Search teacher..."

                        value={search}

                        onChange={(e) =>
                            setSearch(e.target.value)
                        }

                        className="w-full rounded-lg border border-gray-300 pl-10 pr-4 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200"

                    />

                </div>

                <div className="text-sm text-gray-500">

                    {filteredRows.length} Teachers

                </div>

            </div>

            {/* Table */}

            <div className="bg-white rounded-xl shadow border overflow-hidden">

                <div className="overflow-auto">

                    <table className="min-w-full">

                        <thead className="bg-slate-100 sticky top-0">

                            <tr>

                                {[
                                    "Employee ID",
                                    "Teacher",
                                    "Max/Day",
                                    "Min/Day",
                                    "Max/Week",
                                    "Min/Week",
                                    "Max Consecutive",
                                ].map((heading) => (

                                    <th

                                        key={heading}

                                        className="px-4 py-3 text-left text-sm font-semibold text-gray-700 border-b"

                                    >

                                        {heading}

                                    </th>

                                ))}

                            </tr>

                        </thead>

                        <tbody>

                            {filteredRows.map(
                                (
                                    row,
                                    index
                                ) => (

                                    <tr

                                        key={row.teacher}

                                        className="odd:bg-white even:bg-gray-50 hover:bg-blue-50 transition"

                                    >

                                        <td className="px-4 py-3 border-b">

                                            {row.employee_id}

                                        </td>

                                        <td className="px-4 py-3 border-b font-medium">

                                            👨‍🏫 {row.teacher_name}

                                        </td>

                                        {[
                                            "max_periods_per_day",
                                            "min_periods_per_day",
                                            "max_periods_per_week",
                                            "min_periods_per_week",
                                            "max_consecutive_periods",
                                        ].map((field) => (

                                            <td
                                                key={field}
                                                className="px-4 py-3 border-b"
                                            >

                                                <input

                                                    type="number"

                                                    value={row[field]}

                                                    onChange={(e) =>
                                                        handleChange(
                                                            index,
                                                            field,
                                                            e.target.value
                                                        )
                                                    }

                                                    className="w-20 rounded-md border border-gray-300 text-center py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200"

                                                />

                                            </td>

                                        ))}

                                    </tr>

                                )
                            )}

                        </tbody>

                    </table>

                </div>

            </div>

        </div>

    );

};

export default TeacherWorkloadListPage;