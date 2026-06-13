import DraggableTeacher
    from './DraggableTeacher';

const TeacherPalette = ({
    teachers = [],
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
                Teachers
            </h3>

            {

                teachers.map(
                    teacher => (

                        <DraggableTeacher

                            key={teacher.id}

                            teacher={teacher}

                        />

                    )
                )

            }

        </div>

    );

};

export default TeacherPalette;