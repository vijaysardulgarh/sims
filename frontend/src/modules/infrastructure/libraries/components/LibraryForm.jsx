import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const LibraryForm = ({
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
                    '/infrastructure/rooms/?room_type=LIBRARY'
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

                    Library Room
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
                                : 'Select Library Room'
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

            {/* LIBRARY CODE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Library Code
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="LIB-001"
                    value={
                        formData.library_code ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'library_code',
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

            {/* LIBRARIAN */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Librarian

                </label>

                <select
                    value={
                        formData.librarian ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'librarian',
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
                                : 'Select Librarian'
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

            {/* SEATING CAPACITY */}

            <div className="md:col-span-3">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Seating Capacity

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="100"
                    value={
                        formData.seating_capacity ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'seating_capacity',
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

            {/* TOTAL BOOKS */}

            <div className="md:col-span-3">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Total Books

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="5000"
                    value={
                        formData.total_books ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'total_books',
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

            {/* DIGITAL LIBRARY */}

            <div className="md:col-span-6">

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
                            formData.digital_library ||
                            false
                        }
                        onChange={(e) =>
                            handleChange(
                                'digital_library',
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

                            Digital Library

                        </p>

                        <p className="text-sm text-gray-500">

                            Library provides
                            digital resources and
                            online access.

                        </p>

                    </div>

                </label>

            </div>

            {/* INTERNET */}

            <div className="md:col-span-6">

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

                    <div>

                        <p className="font-medium text-gray-700">

                            Internet Enabled

                        </p>

                        <p className="text-sm text-gray-500">

                            Internet access is
                            available in the library.

                        </p>

                    </div>

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

                            Library is currently
                            operational and available.

                        </p>

                    </div>

                </label>

            </div>

        </div>
    );
};

export default LibraryForm;