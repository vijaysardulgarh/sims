import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const ClassroomForm = ({
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
                    Classroom Code
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.classroom_code
                        || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            classroom_code:
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
                        formData.smart_classroom
                        || false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            smart_classroom:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Smart Classroom
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.air_conditioned
                        || false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            air_conditioned:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Air Conditioned
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.projector_available
                        || false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            projector_available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Projector Available
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.whiteboard_available
                        ?? true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            whiteboard_available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Whiteboard Available
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.internet_enabled
                        || false
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
                        formData.is_active
                        ?? true
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

export default ClassroomForm;