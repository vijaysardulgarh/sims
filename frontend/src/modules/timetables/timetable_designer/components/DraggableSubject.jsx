import {
    useDraggable,
} from '@dnd-kit/core';

const DraggableSubject = ({
    subject,
}) => {

    const {

        attributes,

        listeners,

        setNodeRef,

        transform,

    } = useDraggable({

        id: `subject-${subject.id}`,

        data: {

            type: 'subject',

            subject,

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
                bg-blue-50
                cursor-grab
                hover:bg-blue-100
                transition
            "

        >

            <div
                className="
                    font-medium
                "
            >
                {subject.name}
            </div>

            <div
                className="
                    text-xs
                    text-gray-500
                "
            >
                {subject.code}
            </div>

        </div>

    );

};

export default DraggableSubject;