import {
    useDraggable,
} from '@dnd-kit/core';

const DraggableTeacher = ({
    teacher,
}) => {

    const {

        attributes,

        listeners,

        setNodeRef,

        transform,

    } = useDraggable({

        id:
            `teacher-${teacher.id}`,

        data: {

            type:
                'teacher',

            teacher,

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
                bg-green-50
                cursor-grab
            "

        >

            {teacher.name}

        </div>

    );

};

export default DraggableTeacher;