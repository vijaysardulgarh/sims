import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const AuditoriumForm = ({
    formData,
    setFormData,
}) => {

    const [rooms, setRooms] =
        useState([]);

    const [loadingRooms, setLoadingRooms] =
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

    }, []);

    const loadRooms = async () => {

        try {

            setLoadingRooms(
                true
            );

            const response =
                await api.get(
                    '/infrastructure/rooms/?room_type=AUDITORIUM'
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

    return (

        <div className="grid grid-cols-1 gap-6 md:grid-cols-12">

            {/* ROOM */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Room
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
                                : 'Select Room'
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

            {/* AUDITORIUM CODE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Auditorium Code
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="AUD-001"
                    value={
                        formData.auditorium_code ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'auditorium_code',
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

            {/* SEATING CAPACITY */}

            <div className="md:col-span-4">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Seating Capacity

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="500"
                    value={
                        formData.seating_capacity ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'seating_capacity',
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
                />

            </div>

            {/* STAGE AVAILABLE */}

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
                            formData.stage_available ??
                            true
                        }
                        onChange={(e) =>
                            handleChange(
                                'stage_available',
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

                        Stage Available

                    </span>

                </label>

            </div>

            {/* SOUND SYSTEM */}

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
                            formData.sound_system_available ??
                            true
                        }
                        onChange={(e) =>
                            handleChange(
                                'sound_system_available',
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

                        Sound System

                    </span>

                </label>

            </div>

            {/* PROJECTOR */}

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
                            formData.projector_available ||
                            false
                        }
                        onChange={(e) =>
                            handleChange(
                                'projector_available',
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

                        Projector Available

                    </span>

                </label>

            </div>

            {/* AC */}

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
                            formData.air_conditioned ||
                            false
                        }
                        onChange={(e) =>
                            handleChange(
                                'air_conditioned',
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

                        Air Conditioned

                    </span>

                </label>

            </div>

            {/* GREEN ROOM */}

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
                            formData.green_room_available ||
                            false
                        }
                        onChange={(e) =>
                            handleChange(
                                'green_room_available',
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

                        Green Room Available

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

                            Mark this auditorium as
                            available for use.

                        </p>

                    </div>

                </label>

            </div>

        </div>
    );
};

export default AuditoriumForm;