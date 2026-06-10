import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const LaboratoryForm = ({
    formData,
    setFormData,
}) => {

    const [rooms, setRooms] =
        useState([]);

    const [staff, setStaff] =
        useState([]);

    const [loadingRooms, setLoadingRooms] =
        useState(false);

    const [loadingStaff, setLoadingStaff] =
        useState(false);

    const handleChange = (
        field,
        value
    ) => {

        setFormData(
            (prev) => ({
                ...prev,
                [field]: value,
            })
        );
    };

    useEffect(() => {

        loadRooms();

        loadStaff();

    }, []);

    const loadRooms = async () => {

        try {

            setLoadingRooms(
                true
            );

            const response =
                await api.get(
                    '/infrastructure/rooms/?room_type=LABORATORY'
                );

            setRooms(

                response.data.results ||

                response.data ||

                []
            );

        } catch (error) {

            console.error(
                'Failed to load rooms:',
                error
            );

        } finally {

            setLoadingRooms(
                false
            );
        }
    };

    const loadStaff = async () => {

        try {

            setLoadingStaff(
                true
            );

            const response =
                await api.get(
                    '/staff/profiles/'
                );

            setStaff(

                response.data.results ||

                response.data ||

                []
            );

        } catch (error) {

            console.error(
                'Failed to load staff:',
                error
            );

        } finally {

            setLoadingStaff(
                false
            );
        }
    };

    return (

        <div className="grid grid-cols-1 gap-6 md:grid-cols-12">

            {/* ROOM */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Laboratory Room
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    value={
                        formData.room || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room',
                            Number(
                                e.target.value
                            ) || ''
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                >

                    <option value="">

                        {
                            loadingRooms
                                ? 'Loading Rooms...'
                                : 'Select Laboratory Room'
                        }

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

                                {' - '}

                                {
                                    room.room_name
                                }

                            </option>
                        )
                    )}

                </select>

            </div>

            {/* LAB CODE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Laboratory Code
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="LAB-001"
                    value={
                        formData.lab_code ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'lab_code',
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                />

            </div>

            {/* LAB TYPE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Laboratory Type
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    value={
                        formData.lab_type ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'lab_type',
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                >

                    <option value="">
                        Select Laboratory Type
                    </option>

                    <option value="PHYSICS">
                        Physics
                    </option>

                    <option value="CHEMISTRY">
                        Chemistry
                    </option>

                    <option value="BIOLOGY">
                        Biology
                    </option>

                    <option value="COMPUTER">
                        Computer
                    </option>

                    <option value="MATHEMATICS">
                        Mathematics
                    </option>

                    <option value="LANGUAGE">
                        Language
                    </option>

                    <option value="ROBOTICS">
                        Robotics
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

            </div>

            {/* INCHARGE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Laboratory Incharge

                </label>

                <select
                    value={
                        formData.incharge ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'incharge',
                            Number(
                                e.target.value
                            ) || ''
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                >

                    <option value="">

                        {
                            loadingStaff
                                ? 'Loading Staff...'
                                : 'Select Incharge'
                        }

                    </option>

                    {staff.map(
                        (
                            member
                        ) => (

                            <option
                                key={
                                    member.id
                                }
                                value={
                                    member.id
                                }
                            >

                                {
                                    member.full_name
                                }

                            </option>
                        )
                    )}

                </select>

            </div>

            {/* EQUIPMENT COUNT */}

            <div className="md:col-span-4">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Equipment Count

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="50"
                    value={
                        formData.equipment_count ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'equipment_count',
                            Number(
                                e.target.value
                            ) || 0
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                />

            </div>

            {/* SAFETY EQUIPMENT */}

            <div className="md:col-span-4">

                <label
                    className="
                        flex
                        cursor-pointer
                        items-center
                        gap-3
                        rounded-lg
                        border
                        border-gray-200
                        p-4
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.safety_equipment_available ??
                            true
                        }
                        onChange={(e) =>
                            handleChange(
                                'safety_equipment_available',
                                e.target.checked
                            )
                        }
                        className="
                            h-4
                            w-4
                            rounded
                            border-gray-300
                        "
                    />

                    <span className="text-sm font-medium text-gray-700">

                        Safety Equipment

                    </span>

                </label>

            </div>

            {/* INTERNET */}

            <div className="md:col-span-4">

                <label
                    className="
                        flex
                        cursor-pointer
                        items-center
                        gap-3
                        rounded-lg
                        border
                        border-gray-200
                        p-4
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.internet_enabled ||
                            false
                        }
                        onChange={(e) =>
                            handleChange(
                                'internet_enabled',
                                e.target.checked
                            )
                        }
                        className="
                            h-4
                            w-4
                            rounded
                            border-gray-300
                        "
                    />

                    <span className="text-sm font-medium text-gray-700">

                        Internet Enabled

                    </span>

                </label>

            </div>

            {/* ACTIVE */}

            <div className="md:col-span-12">

                <label
                    className="
                        flex
                        cursor-pointer
                        items-center
                        gap-3
                        rounded-lg
                        border
                        border-gray-200
                        p-4
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.is_active ??
                            true
                        }
                        onChange={(e) =>
                            handleChange(
                                'is_active',
                                e.target.checked
                            )
                        }
                        className="
                            h-4
                            w-4
                            rounded
                            border-gray-300
                        "
                    />

                    <div>

                        <p className="font-medium text-gray-700">

                            Active

                        </p>

                        <p className="text-sm text-gray-500">

                            Laboratory is available
                            for use.

                        </p>

                    </div>

                </label>

            </div>

        </div>
    );
};

export default LaboratoryForm;