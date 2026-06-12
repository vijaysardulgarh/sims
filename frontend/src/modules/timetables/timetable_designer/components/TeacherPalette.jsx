import {
    useEffect,
    useState,
} from 'react';

import api
    from '../../../../services/api/axios';

const TeacherPalette = ({
    onSelectTeacher,
    selectedTeacher,
}) => {

    const [teachers, setTeachers] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const loadTeachers =
        async () => {

            try {

                const response =

                    await api.get(
                        '/staff/teachers/'
                    );

                setTeachers(

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

            loadTeachers();

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
                    Teachers
                </h3>

                <span
                    className="
                        text-xs
                        text-gray-500
                    "
                >
                    {teachers.length}
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

                    teachers.map(
                        teacher => (

                            <button

                                key={
                                    teacher.id
                                }

                                type="button"

                                onClick={() =>
                                    onSelectTeacher?.(
                                        teacher
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
                                        selectedTeacher?.id ===
                                        teacher.id

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

                                        teacher.full_name ||

                                        teacher.name ||

                                        teacher.employee_name

                                    }

                                </div>

                                {

                                    teacher.employee_code && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >

                                            Employee Code:
                                            {' '}
                                            {
                                                teacher.employee_code
                                            }

                                        </div>

                                    )

                                }

                                {

                                    teacher.department_name && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >

                                            {
                                                teacher.department_name
                                            }

                                        </div>

                                    )

                                }

                                {

                                    teacher.designation_name && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >

                                            {
                                                teacher.designation_name
                                            }

                                        </div>

                                    )

                                }

                                {

                                    teacher.subjects && (

                                        <div
                                            className="
                                                text-xs
                                                text-gray-500
                                            "
                                        >

                                            Subjects:
                                            {' '}
                                            {
                                                Array.isArray(
                                                    teacher.subjects
                                                )

                                                    ? teacher.subjects.join(
                                                          ', '
                                                      )

                                                    : teacher.subjects
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

export default TeacherPalette;