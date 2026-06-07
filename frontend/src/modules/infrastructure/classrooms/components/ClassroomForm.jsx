import {
    useEffect,
    useState
} from "react";

import api from "../../../../services/api/axios";

const ClassroomForm = ({

    initialData = {},

    onSubmit,

    loading = false,

}) => {

    const [rooms, setRooms] =
        useState([]);

    const [floors, setFloors] =
        useState([]);

    const [formData, setFormData] =
        useState({

            room: "",

            floor: "",

            classroom_code: "",

            capacity: "",

            description: "",

            smart_classroom: false,

            air_conditioned: false,

            projector_available: false,

            whiteboard_available: true,

            internet_enabled: false,
        });

    // ==========================================
    // INITIAL DATA
    // ==========================================

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData({

                room:
                    initialData.room || "",

                floor:
                    initialData.floor || "",

                classroom_code:
                    initialData.classroom_code || "",

                capacity:
                    initialData.capacity || "",

                description:
                    initialData.description || "",

                smart_classroom:
                    initialData.smart_classroom || false,

                air_conditioned:
                    initialData.air_conditioned || false,

                projector_available:
                    initialData.projector_available || false,

                whiteboard_available:
                    initialData.whiteboard_available ?? true,

                internet_enabled:
                    initialData.internet_enabled || false,
            });
        }

    }, [initialData]);

    // ==========================================
    // LOAD MASTER DATA
    // ==========================================

    useEffect(() => {

        loadRooms();

        loadFloors();

    }, []);

    // ==========================================
    // LOAD ROOMS
    // ==========================================

    const loadRooms = async () => {

        try {

            const response =
                await api.get(
                    "/infrastructure/rooms/"
                );

            setRooms(

                response.data.results ||

                response.data ||

                []
            );

        } catch (error) {

            console.error(
                "Failed to load rooms",
                error
            );
        }
    };

    // ==========================================
    // LOAD FLOORS
    // ==========================================

    const loadFloors = async () => {

        try {

            const response =
                await api.get(
                    "/infrastructure/floors/"
                );

            setFloors(

                response.data.results ||

                response.data ||

                []
            );

        } catch (error) {

            console.error(
                "Failed to load floors",
                error
            );
        }
    };

    // ==========================================
    // HANDLE CHANGE
    // ==========================================

    const handleChange = (
        e
    ) => {

        const {

            name,

            value

        } = e.target;

        setFormData(

            (prev) => ({

                ...prev,

                [name]: value,
            })
        );
    };

    // ==========================================
    // HANDLE CHECKBOX
    // ==========================================

    const handleCheckbox = (
        e
    ) => {

        const {

            name,

            checked

        } = e.target;

        setFormData(

            (prev) => ({

                ...prev,

                [name]: checked,
            })
        );
    };

    // ==========================================
    // SUBMIT
    // ==========================================

    const handleSubmit = (
        e
    ) => {

        e.preventDefault();

        onSubmit({

            ...formData,

            room:
                Number(
                    formData.room
                ),

            floor:
                formData.floor
                    ? Number(
                          formData.floor
                      )
                    : null,

            capacity:
                Number(
                    formData.capacity
                ),
        });
    };

    return (

        <form
            onSubmit={
                handleSubmit
            }
            className="
                bg-white
                p-6
                rounded-2xl
                shadow
                space-y-6
            "
        >

            {/* ROOM */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Room
                </label>

                <select

                    name="room"

                    value={
                        formData.room
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "

                    required
                >

                    <option value="">
                        Select Room
                    </option>

                    {rooms.map(
                        (
                            room
                        ) => (

                            <option
                                key={
                                    room.id
                                }
                                value={
                                    room.id
                                }
                            >
                                {
                                    room.room_number
                                }

                                {" - "}

                                {
                                    room.room_name
                                }

                            </option>
                        )
                    )}

                </select>

            </div>

            {/* FLOOR */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Floor
                </label>

                <select

                    name="floor"

                    value={
                        formData.floor
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "
                >

                    <option value="">
                        Select Floor
                    </option>

                    {floors.map(
                        (
                            floor
                        ) => (

                            <option
                                key={
                                    floor.id
                                }
                                value={
                                    floor.id
                                }
                            >
                                {
                                    floor.name
                                }
                            </option>
                        )
                    )}

                </select>

            </div>

            {/* CLASSROOM CODE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Classroom Code
                </label>

                <input

                    type="text"

                    name="classroom_code"

                    value={
                        formData.classroom_code
                    }

                    onChange={
                        handleChange
                    }

                    placeholder="CR-101"

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "

                    required
                />

            </div>

            {/* CAPACITY */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Capacity
                </label>

                <input

                    type="number"

                    name="capacity"

                    value={
                        formData.capacity
                    }

                    onChange={
                        handleChange
                    }

                    min="1"

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "
                />

            </div>

            {/* DESCRIPTION */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Description
                </label>

                <textarea

                    name="description"

                    value={
                        formData.description
                    }

                    onChange={
                        handleChange
                    }

                    rows="4"

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "
                />

            </div>

            {/* FEATURES */}

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-4
                "
            >

                <label>

                    <input

                        type="checkbox"

                        name="smart_classroom"

                        checked={
                            formData.smart_classroom
                        }

                        onChange={
                            handleCheckbox
                        }
                    />

                    {" "}
                    Smart Classroom

                </label>

                <label>

                    <input

                        type="checkbox"

                        name="air_conditioned"

                        checked={
                            formData.air_conditioned
                        }

                        onChange={
                            handleCheckbox
                        }
                    />

                    {" "}
                    Air Conditioned

                </label>

                <label>

                    <input

                        type="checkbox"

                        name="projector_available"

                        checked={
                            formData.projector_available
                        }

                        onChange={
                            handleCheckbox
                        }
                    />

                    {" "}
                    Projector Available

                </label>

                <label>

                    <input

                        type="checkbox"

                        name="whiteboard_available"

                        checked={
                            formData.whiteboard_available
                        }

                        onChange={
                            handleCheckbox
                        }
                    />

                    {" "}
                    Whiteboard Available

                </label>

                <label>

                    <input

                        type="checkbox"

                        name="internet_enabled"

                        checked={
                            formData.internet_enabled
                        }

                        onChange={
                            handleCheckbox
                        }
                    />

                    {" "}
                    Internet Enabled

                </label>

            </div>

            {/* SUBMIT */}

            <button

                type="submit"

                disabled={
                    loading
                }

                className="
                    bg-blue-600
                    text-white
                    px-6
                    py-3
                    rounded-xl
                    hover:bg-blue-700
                    disabled:opacity-50
                "
            >

                {loading

                    ? "Saving..."

                    : "Save Classroom"}

            </button>

        </form>
    );
};

export default ClassroomForm;