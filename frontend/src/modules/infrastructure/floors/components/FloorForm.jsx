import { useEffect, useState } from 'react';

import api from '../../../../services/api/axios';

const FloorForm = ({
    formData,
    setFormData,
}) => {

    const [buildings, setBuildings] =
        useState([]);

    useEffect(() => {

        loadBuildings();

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
                    Floor Name
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.name || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            name:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Floor Number
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.floor_number ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            floor_number:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Description
                </label>

                <textarea
                    className="form-control"
                    value={
                        formData.description ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            description:
                                e.target.value,
                        })
                    }
                />

            </div>
        </>
    );
};

export default FloorForm;