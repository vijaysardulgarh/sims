import DraggableSubject
    from './DraggableSubject';

const SubjectPalette = ({
    subjects = [],
}) => {

    return (

        <div
            className="
                bg-white
                border
                rounded-lg
                p-4
                space-y-3
            "
        >

            <h3
                className="
                    text-lg
                    font-semibold
                "
            >
                Subjects
            </h3>

            {

                subjects.map(
                    subject => (

                        <DraggableSubject

                            key={subject.id}

                            subject={subject}

                        />

                    )
                )

            }

        </div>

    );

};

export default SubjectPalette;