import { useEffect, useState } from 'react';

import api from '../../../../services/api/axios';

const RoomForm = ({
    formData,
    setFormData,
}) => {

    const [buildings, setBuildings] =
        useState([]);

    const [floors, setFloors] =
        useState([]);

    const [loading, setLoading] =
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
    // LOAD INITIAL DATA
    // ==========================================

    useEffect(() => {

        loadBuildings();

    }, []);

    // ==========================================
    // LOAD FLOORS BY BUILDING
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

                setLoading(true);

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

                setLoading(false);
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
            }
        };

    return (

        <div className="row">

            {/* BUILDING */}

            <div className="col-md-6 mb-3">

                <label className="form-label">

                    Building

                </label>

                <select
                    className="form-control"
                    value={
                        formData.building || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'building',
                            Number(
                                e.target.value
                            ) || ''
                        )
                    }
                >

                    <option value="">

                        Select Building

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
                                    building.name
                                }
                            </option>
                        )
                    )}

                </select>

            </div>

            {/* FLOOR */}

            <div className="col-md-6 mb-3">

                <label className="form-label">

                    Floor

                </label>

                <select
                    className="form-control"
                    value={
                        formData.floor || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'floor',
                            Number(
                                e.target.value
                            ) || ''
                        )
                    }
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

            {/* ROOM NUMBER */}

            <div className="col-md-6 mb-3">

                <label className="form-label">

                    Room Number

                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.room_number || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room_number',
                            e.target.value
                        )
                    }
                />

            </div>

            {/* ROOM NAME */}

            <div className="col-md-6 mb-3">

                <label className="form-label">

                    Room Name

                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.room_name || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room_name',
                            e.target.value
                        )
                    }
                />

            </div>

            {/* ROOM TYPE */}

            <div className="col-md-6 mb-3">

                <label className="form-label">

                    Room Type

                </label>

                <select
                    className="form-control"
                    value={
                        formData.room_type || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'room_type',
                            e.target.value
                        )
                    }
                >

                    <option value="">
                        Select Type
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
                        Store
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

            <div className="col-md-3 mb-3">

                <label className="form-label">

                    Area (sq.ft)

                </label>

                <input
                    type="number"
                    min="0"
                    className="form-control"
                    value={
                        formData.area || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'area',
                            e.target.value
                        )
                    }
                />

            </div>

            {/* CAPACITY */}

            <div className="col-md-3 mb-3">

                <label className="form-label">

                    Capacity

                </label>

                <input
                    type="number"
                    min="0"
                    className="form-control"
                    value={
                        formData.capacity || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'capacity',
                            e.target.value
                        )
                    }
                />

            </div>

            {loading && (

                <div className="col-12">

                    Loading...

                </div>

            )}

        </div>
    );
};

export default RoomForm;