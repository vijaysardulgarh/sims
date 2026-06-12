import {
    useEffect,
    useState,
} from 'react';

import api
    from '../../../../services/api/axios';

const SubjectPalette = ({
    onSelectSubject,
    selectedSubject,
}) => {

    const [subjects, setSubjects] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const loadSubjects =
        async () => {

            try {

                const response =

                    await api.get(
                        '/academics/subjects/'
                    );

                setSubjects(

                    response.data.results ||

                    response.data ||

                    []

                );

            }

            catch (error) {

                console.error(
                    error
                );

            }

            finally {

                setLoading(
                    false
                );

            }

        };

    useEffect(
        () => {

            loadSubjects();

        },
        []
    );

    return (

        <div
            className="
                bg-white
                rounded-xl
                shadow
                p-4
                h-full
            "
        >

            <div
                className="
                    flex
                    items-center
                    justify-between
                    mb-4
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

                <span
                    className="
                        text-xs
                        text-gray-500
                    "
                >
                    {subjects.length}
                </span>

            </div>

            {

                loading && (

                    <div
                        className="
                            text-center
                            py-4
                        "
                    >

                        Loading...

                    </div>

                )

            }

            <div
                className="
                    space-y-2
                    max-h-[700px]
                    overflow-y-auto
                "
            >

                {

                    subjects.map(
                        subject => (

                            <button

                                key={
                                    subject.id
                                }

                                type="button"

                                onClick={() =>
                                    onSelectSubject?.(
                                        subject
                                    )
                                }

                                className={`

                                    w-full
                                    text-left
                                    border
                                    rounded-xl
                                    p-3
                                    transition

                                    ${
                                        selectedSubject?.id ===
                                        subject.id

                                            ? `
                                                border-blue-500
                                                bg-blue-50
                                              `

                                            : `
                                                border-gray-200
                                                hover:border-blue-300
                                                hover:bg-gray-50
                                              `
                                    }

                                `}
                            >

                                <div
                                    className="
                                        font-medium
                                    "
                                >
                                    {

                                        subject.name ||

                                        subject.subject_name

                                    }
                                </div>

                                {

                                    subject.code && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >
                                            Code:
                                            {' '}
                                            {
                                                subject.code
                                            }
                                        </div>

                                    )

                                }

                                {

                                    subject.subject_type && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >
                                            {
                                                subject.subject_type
                                            }
                                        </div>

                                    )

                                }

                                {

                                    subject.periods_per_week && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >
                                            Periods/Week:
                                            {' '}
                                            {
                                                subject.periods_per_week
                                            }
                                        </div>

                                    )

                                }

                            </button>

                        )
                    )

                }

            </div>

        </div>

    );

};

export default SubjectPalette;