import {
    useDraggable,
} from '@dnd-kit/core';

const TimetableCell = ({
    entry,
}) => {

    if (!entry) {

        return (

            <div
                className="
                    h-24
                    border-2
                    border-dashed
                    border-gray-300
                    rounded-lg
                    bg-gray-50
                    flex
                    items-center
                    justify-center
                    text-gray-400
                    text-sm
                "
            >

                Drop Subject

            </div>

        );

    }

    const {

        attributes,

        listeners,

        setNodeRef,

        transform,

    } = useDraggable({

        id:
            `entry-${entry.id}`,

        data: {

            type:
                'entry',

            entry,

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

    const isEmpty =

        !entry.subject_name

        &&

        !entry.teacher_name;

    return (

        <div

            ref={setNodeRef}

            style={style}

            {...listeners}

            {...attributes}

            className={

                isEmpty

                ?

                `
                h-24
                border-2
                border-dashed
                border-blue-300
                rounded-lg
                bg-blue-50
                p-2
                cursor-grab
                hover:bg-blue-100
                transition
                `

                :

                `
                h-24
                border
                rounded-lg
                bg-blue-50
                p-2
                cursor-grab
                hover:bg-blue-100
                transition
                `
            }

        >

            <div
                className="
                    font-semibold
                "
            >

                {
                    entry.subject_name
                    ||
                    'Drop Subject'
                }

            </div>

            <div
                className="
                    text-sm
                    text-gray-600
                "
            >

                {
                    entry.teacher_name
                    ||
                    ''
                }

            </div>

            <div
                className="
                    text-xs
                    text-gray-500
                "
            >

                {
                    entry.room_name
                    ||
                    entry.period_name
                    ||
                    ''
                }

            </div>

        </div>

    );

};

export default TimetableCell;