const ConflictPanel = ({
    conflicts = [],
}) => {

    return (

        <div
            className="
                bg-white
                rounded-xl
                shadow
                p-4
            "
        >

            <h3
                className="
                    font-bold
                    mb-4
                "
            >
                Conflicts
            </h3>

            {

                conflicts.map(
                    conflict => (

                        <div
                            key={conflict.id}
                            className="
                                p-2
                                border-b
                            "
                        >

                            {conflict.message}

                        </div>

                    )
                )

            }

        </div>

    );

};

export default ConflictPanel;