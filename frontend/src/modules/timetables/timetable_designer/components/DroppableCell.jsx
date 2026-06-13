import {
    useDroppable,
} from '@dnd-kit/core';

const DroppableCell = ({

    id,

    entryId,

    children,

}) => {

    const {

        isOver,

        setNodeRef,

    } = useDroppable({

        id,

        data: {

            entryId,

        },

    });

    return (

        <div

            ref={setNodeRef}

            className={`

                h-full

                min-h-[90px]

                rounded-lg

                transition-all

                duration-200

                ${

                    isOver

                        ?

                        `
                        bg-green-100
                        border-2
                        border-green-500
                        shadow-md
                        `

                        :

                        `
                        border-2
                        border-transparent
                        `
                }

            `}

        >

            {children}

        </div>

    );

};

export default DroppableCell;