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

    useEffect(() => {

        loadRooms();

    }, []);

    const loadRooms = async () => {

        try {

            const response =
                await api.get(
                    '/infrastructure/rooms/'
                );

            setRooms(
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

                <label className="form-label">
                    Room
                </label>

                <select
                    className="form-control"
                    value={
                        formData.room || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            room:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Room
                    </option>

                    {rooms.map((room) => (
                        <option
                            key={room.id}
                            value={room.id}
                        >
                            {room.room_number}
                            {' - '}
                            {room.room_name}
                        </option>
                    ))}
                </select>

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Lab Code
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.lab_code || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            lab_code:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Lab Type
                </label>

                <select
                    className="form-control"
                    value={
                        formData.lab_type || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            lab_type:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Type
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

            <div className="mb-3">

                <label className="form-label">
                    Incharge
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.incharge || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            incharge:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Equipment Count
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.equipment_count ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            equipment_count:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.safety_equipment_available ||
                        false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            safety_equipment_available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Safety Equipment Available
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.internet_enabled ||
                        false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            internet_enabled:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Internet Enabled
                </label>

            </div>

            <div className="form-check">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.is_active ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            is_active:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Active
                </label>

            </div>
        </>
    );
};

export default LaboratoryForm;