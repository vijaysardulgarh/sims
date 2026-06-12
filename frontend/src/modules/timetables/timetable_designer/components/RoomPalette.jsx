import {
    useEffect,
    useState,
} from 'react';

import api
    from '../../../../services/api/axios';

const RoomPalette = ({
    onSelectRoom,
    selectedRoom,
}) => {

    const [rooms, setRooms] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const loadRooms =
        async () => {

            try {

                const response =

                    await api.get(
                        '/infrastructure/rooms/'
                    );

                setRooms(
                    response.data.results ||
                    response.data ||
                    []
                );

            }

            catch (error) {

                console.error(
                    error
                );

            }

            finally {

                setLoading(
                    false
                );

            }

        };

    useEffect(
        () => {

            loadRooms();

        },
        []
    );

    return (

        <div
            className="
                bg-white
                rounded-xl
                shadow
                p-4
                h-full
            "
        >

            <div
                className="
                    flex
                    items-center
                    justify-between
                    mb-4
                "
            >

                <h3
                    className="
                        text-lg
                        font-semibold
                    "
                >
                    Rooms
                </h3>

                <span
                    className="
                        text-xs
                        text-gray-500
                    "
                >
                    {rooms.length}
                </span>

            </div>

            {

                loading && (

                    <div
                        className="
                            text-center
                            py-4
                        "
                    >

                        Loading...

                    </div>

                )

            }

            <div
                className="
                    space-y-2
                    max-h-[600px]
                    overflow-y-auto
                "
            >

                {

                    rooms.map(
                        room => (

                            <button

                                key={
                                    room.id
                                }

                                type="button"

                                onClick={() =>
                                    onSelectRoom?.(
                                        room
                                    )
                                }

                                className={`

                                    w-full
                                    text-left
                                    border
                                    rounded-xl
                                    p-3
                                    transition

                                    ${
                                        selectedRoom?.id ===
                                        room.id

                                            ? `
                                                border-blue-500
                                                bg-blue-50
                                              `

                                            : `
                                                border-gray-200
                                                hover:border-blue-300
                                                hover:bg-gray-50
                                              `
                                    }

                                `}
                            >

                                <div
                                    className="
                                        font-medium
                                    "
                                >
                                    {

                                        room.room_name ||

                                        room.name ||

                                        room.room_number

                                    }
                                </div>

                                {

                                    room.room_number && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >
                                            Room No:
                                            {' '}
                                            {
                                                room.room_number
                                            }
                                        </div>

                                    )

                                }

                                {

                                    room.capacity && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >
                                            Capacity:
                                            {' '}
                                            {
                                                room.capacity
                                            }
                                        </div>

                                    )

                                }

                                {

                                    room.room_type && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >
                                            {
                                                room.room_type
                                            }
                                        </div>

                                    )

                                }

                            </button>

                        )
                    )

                }

            </div>

        </div>

    );

};

export default RoomPalette;