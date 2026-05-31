import { useState } from "react";

const SchoolSettingForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

            school:
                initialData.school || "",

            academic_year_format:
                initialData.academic_year_format ||
                "2025-2026",

            attendance_type:
                initialData.attendance_type ||
                "DAILY",

            grading_system:
                initialData.grading_system ||
                "MARKS",

            working_days_per_week:
                initialData.working_days_per_week || 6,

            allow_online_admission:
                initialData.allow_online_admission ?? true,
        });

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
        } = e.target;

        setFormData({

            ...formData,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        });
    };

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);
    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                type="number"
                name="school"
                placeholder="School ID"
                value={formData.school}
                onChange={handleChange}
            />

            <input
                type="text"
                name="academic_year_format"
                value={
                    formData.academic_year_format
                }
                onChange={handleChange}
            />

            <select
                name="attendance_type"
                value={
                    formData.attendance_type
                }
                onChange={handleChange}
            >
                <option value="DAILY">
                    Daily
                </option>

                <option value="PERIOD">
                    Period Wise
                </option>

            </select>

            <select
                name="grading_system"
                value={
                    formData.grading_system
                }
                onChange={handleChange}
            >
                <option value="MARKS">
                    Marks
                </option>

                <option value="GRADE">
                    Grade
                </option>

                <option value="BOTH">
                    Both
                </option>

            </select>

            <input
                type="number"
                name="working_days_per_week"
                value={
                    formData.working_days_per_week
                }
                onChange={handleChange}
            />

            <label>

                Online Admission

                <input
                    type="checkbox"
                    name="allow_online_admission"
                    checked={
                        formData.allow_online_admission
                    }
                    onChange={handleChange}
                />

            </label>

            <button type="submit">

                Save

            </button>

        </form>
    );
};

export default SchoolSettingForm;