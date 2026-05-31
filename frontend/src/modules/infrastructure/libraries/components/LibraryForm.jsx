
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
                    Library Code
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.library_code || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            library_code:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Librarian ID
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.librarian || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            librarian:
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

            <div className="mb-3">

                <label className="form-label">
                    Total Books
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.total_books || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            total_books:
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
                        formData.digital_library ||
                        false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            digital_library:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Digital Library
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

export default LibraryForm;