import {
    useEffect,
    useState,
} from "react";

import toast from "react-hot-toast";

import {
    Save,
    Search,
    Users,
} from "lucide-react";

import teacherPreferenceService from "../services/teacherPreferenceService";

const TeacherPreferenceListPage = () => {

    const [preferences, setPreferences] = useState([]);

    const [loading, setLoading] = useState(true);

    const [saving, setSaving] = useState(false);

    const [search, setSearch] = useState("");

    useEffect(() => {

        loadPreferences();

    }, []);

    const loadPreferences = async () => {

        try {

            const { data } =
                await teacherPreferenceService.getAll();

            setPreferences(data);

        } catch {

            toast.error(
                "Failed to load teacher preferences."
            );

        } finally {

            setLoading(false);

        }

    };

    const handleChange = (
        index,
        field,
        value,
    ) => {

        const updated = [...preferences];

        updated[index][field] = value;

        setPreferences(updated);

    };

    const saveAll = async () => {

        try {

            setSaving(true);

            await teacherPreferenceService.saveAll(
                preferences,
            );

            toast.success(
                "Teacher preferences saved successfully."
            );

        } catch {

            toast.error(
                "Failed to save teacher preferences."
            );

        } finally {

            setSaving(false);

        }

    };

    const filtered = preferences.filter((row) => {

        const text = `${row.teacher_name} ${row.employee_id}`.toLowerCase();

        return text.includes(
            search.toLowerCase(),
        );

    });

    if (loading) {

        return (
            <div className="p-6">
                Loading...
            </div>
        );

    }

    return (

        <div className="space-y-6">

            <div className="rounded-xl border bg-white p-6 shadow-sm">

                <div className="flex items-center justify-between">

                    <div>

                        <h1 className="text-2xl font-bold">

                            Teacher Preference Settings

                        </h1>

                        <p className="mt-1 text-sm text-gray-500">

                            Configure timetable preferences for every teacher.

                        </p>

                    </div>

                    <button
                        onClick={saveAll}
                        disabled={saving}
                        className="flex items-center gap-2 rounded-lg bg-blue-600 px-5 py-2 text-white hover:bg-blue-700"
                    >

                        <Save size={18} />

                        {saving
                            ? "Saving..."
                            : "Save All Changes"}

                    </button>

                </div>

            </div>

            <div className="grid grid-cols-1 gap-4 md:grid-cols-3">

                <div className="rounded-lg border bg-white p-4">

                    <div className="flex items-center gap-2">

                        <Users size={18} />

                        <span>Total Teachers</span>

                    </div>

                    <div className="mt-2 text-3xl font-bold">

                        {preferences.length}

                    </div>

                </div>

            </div>

            <div className="rounded-xl border bg-white shadow-sm">

                <div className="border-b p-4">

                    <div className="relative max-w-sm">

                        <Search
                            size={18}
                            className="absolute left-3 top-3 text-gray-400"
                        />

                        <input
                            value={search}
                            onChange={(e) =>
                                setSearch(
                                    e.target.value,
                                )
                            }
                            placeholder="Search teacher..."
                            className="w-full rounded-lg border py-2 pl-10 pr-4"
                        />

                    </div>

                </div>

                <div className="overflow-x-auto">

                    <table className="min-w-full text-sm">

                        <thead className="bg-gray-100">

                            <tr>

                                <th className="px-4 py-3 text-left">
                                    Employee ID
                                </th>

                                <th className="px-4 py-3 text-left">
                                    Teacher
                                </th>

                                <th className="px-4 py-3 text-center">
                                    Prefer First
                                </th>

                                <th className="px-4 py-3 text-center">
                                    Avoid First
                                </th>

                                <th className="px-4 py-3 text-center">
                                    Prefer Last
                                </th>

                                <th className="px-4 py-3 text-center">
                                    Avoid Last
                                </th>

                                <th className="px-4 py-3">
                                    Preferred Shift
                                </th>

                                <th className="px-4 py-3">
                                    Max Free Gaps
                                </th>

                            </tr>

                        </thead>

                        <tbody>

                            {filtered.map(
                                (
                                    row,
                                    index,
                                ) => (

                                    <tr
                                        key={row.teacher}
                                        className="border-t"
                                    >

                                        <td className="px-4 py-3">

                                            {row.employee_id}

                                        </td>

                                        <td className="px-4 py-3">

                                            {row.teacher_name}

                                        </td>

                                        <td className="text-center">

                                            <input
                                                type="checkbox"
                                                checked={
                                                    row.prefer_first_period
                                                }
                                                onChange={(e) =>
                                                    handleChange(
                                                        index,
                                                        "prefer_first_period",
                                                        e.target.checked,
                                                    )
                                                }
                                            />

                                        </td>

                                        <td className="text-center">

                                            <input
                                                type="checkbox"
                                                checked={
                                                    row.avoid_first_period
                                                }
                                                onChange={(e) =>
                                                    handleChange(
                                                        index,
                                                        "avoid_first_period",
                                                        e.target.checked,
                                                    )
                                                }
                                            />

                                        </td>

                                        <td className="text-center">

                                            <input
                                                type="checkbox"
                                                checked={
                                                    row.prefer_last_period
                                                }
                                                onChange={(e) =>
                                                    handleChange(
                                                        index,
                                                        "prefer_last_period",
                                                        e.target.checked,
                                                    )
                                                }
                                            />

                                        </td>

                                        <td className="text-center">

                                            <input
                                                type="checkbox"
                                                checked={
                                                    row.avoid_last_period
                                                }
                                                onChange={(e) =>
                                                    handleChange(
                                                        index,
                                                        "avoid_last_period",
                                                        e.target.checked,
                                                    )
                                                }
                                            />

                                        </td>

                                        <td className="px-4 py-2">

                                            <select
                                                value={
                                                    row.preferred_shift || ""
                                                }
                                                onChange={(e) =>
                                                    handleChange(
                                                        index,
                                                        "preferred_shift",
                                                        e.target.value,
                                                    )
                                                }
                                                className="rounded border px-2 py-1"
                                            >

                                                <option value="">
                                                    No Preference
                                                </option>

                                                <option value="MORNING">
                                                    Morning
                                                </option>

                                                <option value="AFTERNOON">
                                                    Afternoon
                                                </option>

                                            </select>

                                        </td>

                                        <td className="px-4 py-2">

                                            <input
                                                type="number"
                                                min="0"
                                                className="w-20 rounded border px-2 py-1"
                                                value={
                                                    row.maximum_free_gaps
                                                }
                                                onChange={(e) =>
                                                    handleChange(
                                                        index,
                                                        "maximum_free_gaps",
                                                        Number(
                                                            e.target.value,
                                                        ),
                                                    )
                                                }
                                            />

                                        </td>

                                    </tr>

                                ),
                            )}

                        </tbody>

                    </table>

                </div>

            </div>

        </div>

    );

};

export default TeacherPreferenceListPage;