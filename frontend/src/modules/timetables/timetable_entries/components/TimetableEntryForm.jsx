import {
    useEffect,
    useState,
} from "react";

import timetableService
    from "../../timetables/services/timetableService";

import periodDefinitionService
    from "../../period_definitions/services/periodDefinitionService";

import subjectService
    from "../../../academics/subjects/services/subjectService";

import staffService
    from "../../../staff/staff/services/staffService";

const TimetableEntryForm = ({
    formData,
    setFormData,
}) => {

    const [
        timetables,
        setTimetables,
    ] = useState([]);

    const [
        periods,
        setPeriods,
    ] = useState([]);

    const [
        subjects,
        setSubjects,
    ] = useState([]);

    const [
        teachers,
        setTeachers,
    ] = useState([]);

    useEffect(() => {

        loadDropdowns();

    }, []);

    const loadDropdowns =
        async () => {

            try {

                const [

                    timetableResponse,

                    periodResponse,

                    subjectResponse,

                    teacherResponse,

                ] = await Promise.all([

                    timetableService.getAll(),

                    periodDefinitionService.getAll(),

                    subjectService.getSubjects(),

                    staffService.getStaff(),

                ]);

                setTimetables(

                    timetableResponse.data?.results ||

                    timetableResponse.data ||

                    []

                );

                setPeriods(

                    periodResponse.data?.results ||

                    periodResponse.data ||

                    []

                );

                setSubjects(

                    subjectResponse.results ||

                    subjectResponse ||

                    []

                );

                setTeachers(

                    teacherResponse.results ||

                    teacherResponse ||

                    []

                );

            }

            catch (error) {

                console.error(
                    "Dropdown Load Error:",
                    error
                );

            }

        };

    const handleChange =
        (event) => {

            const {
                name,
                value,
            } = event.target;

            setFormData({

                ...formData,

                [name]: value,

            });

        };

    return (

        <div
            className="
                grid
                grid-cols-1
                md:grid-cols-2
                gap-6
            "
        >

            <div>

                <label
                    className="
                        block
                        mb-2
                    "
                >
                    Timetable
                </label>

                <select

                    name="timetable"

                    value={
                        formData.timetable || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Timetable
                    </option>

                    {timetables.map(
                        timetable => (

                            <option
                                key={
                                    timetable.id
                                }
                                value={
                                    timetable.id
                                }
                            >
                                {
                                    timetable.name
                                }
                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                    "
                >
                    Day
                </label>

                <select

                    name="day"

                    value={
                        formData.day || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Day
                    </option>

                    <option value="MON">
                        Monday
                    </option>

                    <option value="TUE">
                        Tuesday
                    </option>

                    <option value="WED">
                        Wednesday
                    </option>

                    <option value="THU">
                        Thursday
                    </option>

                    <option value="FRI">
                        Friday
                    </option>

                    <option value="SAT">
                        Saturday
                    </option>

                    <option value="SUN">
                        Sunday
                    </option>

                </select>

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                    "
                >
                    Period
                </label>

                <select

                    name="period"

                    value={
                        formData.period || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Period
                    </option>

                    {periods.map(
                        period => (

                            <option
                                key={
                                    period.id
                                }
                                value={
                                    period.id
                                }
                            >
                                {
                                    period.name ||

                                    period.period_name ||

                                    `Period ${period.id}`
                                }
                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                    "
                >
                    Subject
                </label>

                <select

                    name="subject"

                    value={
                        formData.subject || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Subject
                    </option>

                    {subjects.map(
                        subject => (

                            <option
                                key={
                                    subject.id
                                }
                                value={
                                    subject.id
                                }
                            >
                                {
                                    subject.name
                                }
                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                    "
                >
                    Teacher
                </label>

                <select

                    name="teacher"

                    value={
                        formData.teacher || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Teacher
                    </option>

                    {teachers.map(
                        teacher => (

                            <option
                                key={
                                    teacher.id
                                }
                                value={
                                    teacher.id
                                }
                            >
                                {
                                    teacher.full_name ||

                                    teacher.name ||

                                    teacher.employee_name ||

                                    `Staff ${teacher.id}`
                                }
                            </option>

                        )
                    )}

                </select>

            </div>

            <div
                className="
                    md:col-span-2
                "
            >

                <label
                    className="
                        block
                        mb-2
                    "
                >
                    Remarks
                </label>

                <textarea

                    name="remarks"

                    value={
                        formData.remarks || ""
                    }

                    onChange={
                        handleChange
                    }

                    rows={4}

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                />

            </div>

        </div>

    );

};

export default TimetableEntryForm;