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
                    Auditorium Code
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.auditorium_code || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            auditorium_code:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Seating Capacity
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.seating_capacity || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            seating_capacity:
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
                        formData.stage_available ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            stage_available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Stage Available
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.sound_system_available ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            sound_system_available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Sound System Available
                </label>

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.projector_available ||
                        false
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
                        formData.air_conditioned ||
                        false
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
                        formData.green_room_available ||
                        false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            green_room_available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Green Room Available
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

export default AuditoriumForm;