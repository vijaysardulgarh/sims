import {
    useEffect,
    useState,
} from "react";

import bellScheduleService
    from "../../bell_schedules/services/bellScheduleService";

const PeriodDefinitionForm = ({
    formData,
    setFormData,
}) => {

    const [
        bellSchedules,
        setBellSchedules,
    ] = useState([]);

    useEffect(() => {

        loadBellSchedules();

    }, []);

    const loadBellSchedules =
        async () => {

            try {

                const response =
                    await bellScheduleService.getAll();

                setBellSchedules(

                    response.data?.results ||

                    response.data ||

                    []

                );

            }

            catch (error) {

                console.error(
                    "Failed to load bell schedules",
                    error
                );

            }

        };

    const handleChange = (
        event
    ) => {

        const {
            name,
            value,
            type,
            checked,
        } = event.target;

        setFormData({

            ...formData,

            [name]:

                type === "checkbox"

                    ? checked

                    : value,

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

                <label>
                    Bell Schedule
                </label>

                <select

                    name="bell_schedule"

                    value={
                        formData.bell_schedule || ""
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
                        Select Bell Schedule
                    </option>

                    {bellSchedules.map(
                        schedule => (

                            <option
                                key={
                                    schedule.id
                                }
                                value={
                                    schedule.id
                                }
                            >
                                {
                                    schedule.name
                                }
                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label>
                    Name
                </label>

                <input
                    type="text"
                    name="name"
                    value={
                        formData.name || ""
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
                />

            </div>

            <div>

                <label>
                    Code
                </label>

                <input
                    type="text"
                    name="code"
                    value={
                        formData.code || ""
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
                />

            </div>

            <div>

                <label>
                    Display Order
                </label>

                <input
                    type="number"
                    name="display_order"
                    value={
                        formData.display_order || ""
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
                />

            </div>

            <div>

                <label>
                    Start Time
                </label>

                <input
                    type="time"
                    name="start_time"
                    value={
                        formData.start_time || ""
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
                />

            </div>

            <div>

                <label>
                    End Time
                </label>

                <input
                    type="time"
                    name="end_time"
                    value={
                        formData.end_time || ""
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
                />

            </div>

            <div>

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input
                        type="checkbox"
                        name="is_instructional"
                        checked={
                            formData.is_instructional ?? true
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Instructional Period

                </label>

            </div>

            <div>

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input
                        type="checkbox"
                        name="is_break"
                        checked={
                            formData.is_break ?? false
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Break

                </label>

            </div>

            <div>

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input
                        type="checkbox"
                        name="is_lunch"
                        checked={
                            formData.is_lunch ?? false
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Lunch

                </label>

            </div>

            <div>

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input
                        type="checkbox"
                        name="is_assembly"
                        checked={
                            formData.is_assembly ?? false
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Assembly

                </label>

            </div>

            <div>

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input
                        type="checkbox"
                        name="is_zero_period"
                        checked={
                            formData.is_zero_period ?? false
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Zero Period

                </label>

            </div>

            <div
                className="
                    md:col-span-2
                "
            >

                <label>
                    Remarks
                </label>

                <textarea

                    name="remarks"

                    rows={4}

                    value={
                        formData.remarks || ""
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
                />

            </div>

        </div>

    );

};

export default PeriodDefinitionForm;