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

    useEffect(() => {

        loadBuildings();
        loadFloors();

    }, []);

    const loadBuildings = async () => {

        try {

            const response =
                await api.get(
                    '/infrastructure/buildings/'
                );

            setBuildings(
                response.data.results ||
                response.data
            );

        } catch (error) {

            console.error(error);
        }
    };

    const loadFloors = async () => {

        try {

            const response =
                await api.get(
                    '/infrastructure/floors/'
                );

            setFloors(
                response.data.results ||
                response.data
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (
        <>
            <div className="mb-3">

                <label>
                    Building
                </label>

                <select
                    className="form-control"
                    value={
                        formData.building || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            building:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Building
                    </option>

                    {buildings.map(
                        (building) => (
                            <option
                                key={building.id}
                                value={building.id}
                            >
                                {building.name}
                            </option>
                        )
                    )}
                </select>

            </div>

            <div className="mb-3">

                <label>
                    Floor
                </label>

                <select
                    className="form-control"
                    value={
                        formData.floor || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            floor:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Floor
                    </option>

                    {floors.map(
                        (floor) => (
                            <option
                                key={floor.id}
                                value={floor.id}
                            >
                                {floor.name}
                            </option>
                        )
                    )}
                </select>

            </div>

            <div className="mb-3">

                <label>
                    Room Number
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.room_number || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            room_number:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Room Name
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.room_name || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            room_name:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Room Type
                </label>

                <select
                    className="form-control"
                    value={
                        formData.room_type || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            room_type:
                                e.target.value,
                        })
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

            <div className="mb-3">

                <label>
                    Area
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.area || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            area:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Capacity
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.capacity || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            capacity:
                                e.target.value,
                        })
                    }
                />

            </div>
        </>
    );
};

export default RoomForm;