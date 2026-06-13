const TimetableVersionPanel = ({
    versions = [],
}) => {

    return (

        <div
            className="
                bg-white
                border
                rounded-lg
                p-4
            "
        >

            <h3
                className="
                    font-semibold
                    mb-3
                "
            >
                Versions
            </h3>

            {

                versions.map(
                    version => (

                        <div
                            key={version.id}
                            className="
                                border-b
                                py-2
                            "
                        >

                            {version.name}

                        </div>

                    )
                )

            }

        </div>

    );

};

export default TimetableVersionPanel;