import { useEffect, useState } from 'react';

import api from '../../../../services/api/axios';

const FloorForm = ({
    formData,
    setFormData,
}) => {

    const [buildings, setBuildings] =
        useState([]);

    const [loadingBuildings, setLoadingBuildings] =
        useState(false);

    useEffect(() => {

        loadBuildings();

    }, []);

    const floorNames = {

        0: 'Ground Floor',

        1: 'First Floor',

        2: 'Second Floor',

        3: 'Third Floor',

        4: 'Fourth Floor',

        5: 'Fifth Floor',

        6: 'Sixth Floor',

        7: 'Seventh Floor',

        8: 'Eighth Floor',

        9: 'Ninth Floor',

        10: 'Tenth Floor',
    };

    const loadBuildings = async () => {

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
                error
            );

        } finally {

            setLoadingBuildings(
                false
            );
        }
    };

    const handleFloorNumberChange = (
        e
    ) => {

        const value =
            e.target.value === ''
                ? ''
                : parseInt(
                    e.target.value,
                    10
                );

        setFormData({

            ...formData,

            floor_number:
                value,

            name:
                floorNames[
                    value
                ] ||
                formData.name ||
                '',
        });
    };

    return (

        <div className="space-y-6">

            {/* Building */}

            <div>

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
                    onChange={(e) =>
                        setFormData({

                            ...formData,

                            building:
                                e.target
                                    .value,
                        })
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

            {/* Floor Number */}

            <div>

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Floor Number
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="number"
                    required
                    min="0"
                    value={
                        formData.floor_number ??
                        ''
                    }
                    onChange={
                        handleFloorNumberChange
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
                    placeholder="Enter floor number"
                />

            </div>

            {/* Floor Name */}

            <div>

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Floor Name
                </label>

                <input
                    type="text"
                    value={
                        formData.name ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({

                            ...formData,

                            name:
                                e.target
                                    .value,
                        })
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        bg-gray-50
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                    placeholder="Floor Name"
                />

            </div>

            {/* Description */}

            <div>

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Description
                </label>

                <textarea
                    rows={4}
                    value={
                        formData.description ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({

                            ...formData,

                            description:
                                e.target
                                    .value,
                        })
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
                    placeholder="Enter description"
                />

            </div>

        </div>
    );
};

export default FloorForm;