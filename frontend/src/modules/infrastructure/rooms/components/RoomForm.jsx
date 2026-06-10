import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const RoomForm = ({
    formData,
    setFormData,
}) => {

    const [buildings, setBuildings] =
        useState([]);

    const [floors, setFloors] =
        useState([]);

    const [loadingBuildings, setLoadingBuildings] =
        useState(false);

    const [loadingFloors, setLoadingFloors] =
        useState(false);

    // ==========================================
    // HANDLE CHANGE
    // ==========================================

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

    // ==========================================
    // LOAD BUILDINGS
    // ==========================================

    useEffect(() => {

        loadBuildings();

    }, []);

    // ==========================================
    // LOAD FLOORS
    // ==========================================

    useEffect(() => {

        if (
            formData.building
        ) {

            loadFloors(
                formData.building
            );

        } else {

            setFloors([]);
        }

    }, [
        formData.building
    ]);

    // ==========================================
    // BUILDINGS
    // ==========================================

    const loadBuildings =
        async () => {

            try {

                setLoadingBuildings(
                    true
                );

                const response =
                    await api.get(
                        '/infrastructure/buildings/'
                    );

                setBuildings(

                    response.data.results ||

                    response.data ||

                    []
                );

            } catch (error) {

                console.error(
                    'Failed to load buildings:',
                    error
                );

            } finally {

                setLoadingBuildings(
                    false
                );
            }
        };

    // ==========================================
    // FLOORS
    // ==========================================

    const loadFloors =
        async (
            buildingId
        ) => {

            try {

                setLoadingFloors(
                    true
                );

                const response =
                    await api.get(
                        `/infrastructure/floors/?building=${buildingId}`
                    );

                setFloors(

                    response.data.results ||

                    response.data ||

                    []
                );

            } catch (error) {

                console.error(
                    'Failed to load floors:',
                    error
                );

            } finally {

                setLoadingFloors(
                    false
                );
            }
        };

    return (

        <div className="grid grid-cols-1 gap-6 md:grid-cols-12">

            {/* BUILDING */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Building
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    value={
                        formData.building ||
                        ''
                    }
                    onChange={(e) => {

                        const buildingId =
                            Number(
                                e.target.value
                            ) || '';

                        setFormData(
                            (prev) => ({
                                ...prev,
                                building:
                                    buildingId,
                                floor: '',
                            })
                        );
                    }}
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
                            loadingBuildings
                                ? 'Loading Buildings...'
                                : 'Select Building'
                        }

                    </option>

                    {buildings.map(
                        (
                            building
                        ) => (

                            <option
                                key={
                                    building.id
                                }
                                value={
                                    building.id
                                }
                            >

                                {
                                    building.code
                                }

                                {' - '}

                                {
                                    building.name
                                }

                            </option>
                        )
                    )}

                </select>

            </div>

            {/* FLOOR */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Floor
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    disabled={
                        !formData.building
                    }
                    value={
                        formData.floor ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'floor',
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
                        disabled:bg-gray-100
                        disabled:cursor-not-allowed
                    "
                >

                    <option value="">

                        {
                            loadingFloors
                                ? 'Loading Floors...'
                                : 'Select Floor'
                        }

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
                                    floor.floor_number
                                }

                                {' - '}

                                {
                                    floor.name
                                }

                            </option>
                        )
                    )}

                </select>

            </div>

            {/* ROOM NUMBER */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Room Number
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="101"
                    value={
                        formData.room_number ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room_number',
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

            {/* ROOM NAME */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Room Name
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="Physics Laboratory"
                    value={
                        formData.room_name ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room_name',
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

            {/* ROOM TYPE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Room Type
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    value={
                        formData.room_type ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room_type',
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
                        Select Room Type
                    </option>

                    <option value="CLASSROOM">
                        Classroom
                    </option>

                    <option value="LABORATORY">
                        Laboratory
                    </option>

                    <option value="LIBRARY">
                        Library
                    </option>

                    <option value="OFFICE">
                        Office
                    </option>

                    <option value="STAFF_ROOM">
                        Staff Room
                    </option>

                    <option value="STORE">
                        Store Room
                    </option>

                    <option value="AUDITORIUM">
                        Auditorium
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

            </div>

            {/* AREA */}

            <div className="md:col-span-3">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Area (sq.ft)

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="500"
                    value={
                        formData.area || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'area',
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

            {/* CAPACITY */}

            <div className="md:col-span-3">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Capacity

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="40"
                    value={
                        formData.capacity || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'capacity',
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

        </div>
    );
};

export default RoomForm;