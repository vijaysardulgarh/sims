// ============================================
// CLASS INCHARGE FORM
// File: ClassInchargeForm.jsx
// ============================================

import { useEffect, useMemo, useState } from "react";

import classService from "../../../academics/classes/services/classService";
import sectionService from "../../../academics/sections/services/sectionService";
import staffService from "../../staff/services/staffService";

const ClassInchargeForm = ({
    initialData = {},
    onSubmit,
    loading = false,
}) => {

    const [classes, setClasses] = useState([]);
    const [sections, setSections] = useState([]);
    const [teachers, setTeachers] = useState([]);

    const [formData, setFormData] = useState({
        student_class: "",
        section: "",
        staff: "",
        effective_from: "",
        effective_to: "",
        active: true,
        remarks: "",
    });

    // ============================================
    // LOAD DATA
    // ============================================

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {

        try {

            const [
                classResponse,
                sectionResponse,
                staffResponse,
            ] = await Promise.all([
                classService.getClasses(),
                sectionService.getSections(),
                staffService.getStaff(),
            ]);

            const classList = Array.isArray(classResponse)
                ? classResponse
                : classResponse.results || [];

            const sectionList = Array.isArray(sectionResponse)
                ? sectionResponse
                : sectionResponse.results || [];

            const staffList = Array.isArray(staffResponse)
                ? staffResponse
                : staffResponse.results || [];

            setClasses(classList);

            setSections(sectionList);

            setTeachers(
                staffList.filter(
                    (item) =>
                        item.staff_role === "Teaching" &&
                        item.is_active
                )
            );

        } catch (error) {

            console.error(error);

        }

    };

    // ============================================
    // PREFILL
    // ============================================

    useEffect(() => {

        if (!initialData?.id) return;

        const selectedSection = sections.find(
            (s) => s.id === initialData.section
        );

        setFormData({

            student_class:
                selectedSection?.class_obj?.id ||
                selectedSection?.class_obj ||
                "",

            section: initialData.section || "",

            staff: initialData.staff || "",

            effective_from:
                initialData.effective_from || "",

            effective_to:
                initialData.effective_to || "",

            active:
                initialData.active ?? true,

            remarks:
                initialData.remarks || "",

        });

    }, [initialData, sections]);

    // ============================================
    // FILTERED SECTIONS
    // ============================================

    const filteredSections = useMemo(() => {

        return sections.filter((item) =>

            String(
                item.class_obj?.id ||
                item.class_obj
            ) ===
            String(formData.student_class)

        );

    }, [sections, formData.student_class]);

    // ============================================
    // CHANGE
    // ============================================

    const handleChange = (e) => {

        const { name, value, type, checked } = e.target;

        if (name === "student_class") {

            setFormData((prev) => ({
                ...prev,
                student_class: value,
                section: "",
            }));

            return;

        }

        setFormData((prev) => ({
            ...prev,
            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        }));

    };

    // ============================================
    // SUBMIT
    // ============================================

    const handleSubmit = (e) => {

        e.preventDefault();

        if (!formData.section) {

            alert("Please select section.");

            return;

        }

        if (!formData.staff) {

            alert("Please select teacher.");

            return;

        }

        if (
            formData.effective_to &&
            formData.effective_to <
            formData.effective_from
        ) {

            alert(
                "Effective To must be after Effective From."
            );

            return;

        }

        onSubmit(formData);

    };

    return (

        <form
            onSubmit={handleSubmit}
            className="bg-white rounded-xl shadow p-6 space-y-6"
        >

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                {/* Class */}

                <div>

                    <label className="block mb-2 font-medium">
                        Class
                    </label>

                    <select
                        name="student_class"
                        value={formData.student_class}
                        onChange={handleChange}
                        required
                        className="w-full border rounded-lg px-4 py-3"
                    >

                        <option value="">
                            Select Class
                        </option>

                        {classes.map((item) => (

                            <option
                                key={item.id}
                                value={item.id}
                            >
                                {item.name}
                            </option>

                        ))}

                    </select>

                </div>

                {/* Section */}

                <div>

                    <label className="block mb-2 font-medium">
                        Section
                    </label>

                    <select
                        name="section"
                        value={formData.section}
                        onChange={handleChange}
                        required
                        className="w-full border rounded-lg px-4 py-3"
                    >

                        <option value="">
                            Select Section
                        </option>

                        {filteredSections.map((item) => (

                            <option
                                key={item.id}
                                value={item.id}
                            >
                                {item.name}
                            </option>

                        ))}

                    </select>

                </div>

                {/* Teacher */}

                <div>

                    <label className="block mb-2 font-medium">
                        Teacher
                    </label>

                    <select
                        name="staff"
                        value={formData.staff}
                        onChange={handleChange}
                        required
                        className="w-full border rounded-lg px-4 py-3"
                    >

                        <option value="">
                            Select Teacher
                        </option>

                        {teachers.map((item) => (

                            <option
                                key={item.id}
                                value={item.id}
                            >
                                {item.employee_id} - {item.name}
                            </option>

                        ))}

                    </select>

                </div>

                {/* Effective From */}

                <div>

                    <label className="block mb-2 font-medium">
                        Effective From
                    </label>

                    <input
                        type="date"
                        name="effective_from"
                        value={formData.effective_from}
                        onChange={handleChange}
                        required
                        className="w-full border rounded-lg px-4 py-3"
                    />

                </div>

                {/* Effective To */}

                <div>

                    <label className="block mb-2 font-medium">
                        Effective To
                    </label>

                    <input
                        type="date"
                        name="effective_to"
                        value={formData.effective_to}
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-3"
                    />

                </div>

            </div>

            {/* Remarks */}

            <div>

                <label className="block mb-2 font-medium">
                    Remarks
                </label>

                <textarea
                    name="remarks"
                    value={formData.remarks}
                    onChange={handleChange}
                    rows={3}
                    className="w-full border rounded-lg px-4 py-3"
                />

            </div>

            {/* Active */}

            <label className="flex items-center gap-3">

                <input
                    type="checkbox"
                    name="active"
                    checked={formData.active}
                    onChange={handleChange}
                />

                Active Assignment

            </label>

            {/* Submit */}

            <button
                type="submit"
                disabled={loading}
                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
            >
                {loading ? "Saving..." : "Save Class Incharge"}
            </button>

        </form>
    );
};

export default ClassInchargeForm;