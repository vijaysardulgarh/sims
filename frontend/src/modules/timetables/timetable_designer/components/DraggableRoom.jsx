import {
    useDraggable,
} from '@dnd-kit/core';

const DraggableRoom = ({
    room,
}) => {

    const {

        attributes,

        listeners,

        setNodeRef,

        transform,

    } = useDraggable({

        id:
            `room-${room.id}`,

        data: {

            type:
                'room',

            room,

        },

    });

    const style = transform
        ? {
              transform:
                  `translate3d(
                    ${transform.x}px,
                    ${transform.y}px,
                    0
                )`,
          }
        : undefined;

    return (

        <div

            ref={setNodeRef}

            style={style}

            {...listeners}

            {...attributes}

            className="
                p-3
                rounded-lg
                border
                bg-yellow-50
                cursor-grab
            "

        >

            {room.room_name}

        </div>

    );

};

export default DraggableRoom;