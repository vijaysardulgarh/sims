import DraggableRoom
    from './DraggableRoom';

const RoomPalette = ({
    rooms = [],
}) => {

    return (

        <div
            className="
                bg-white
                border
                rounded-lg
                p-4
                space-y-2
            "
        >

            <h3
                className="
                    font-semibold
                "
            >
                Rooms
            </h3>

            {

                rooms.map(
                    room => (

                        <DraggableRoom

                            key={room.id}

                            room={room}

                        />

                    )
                )

            }

        </div>

    );

};

export default RoomPalette;