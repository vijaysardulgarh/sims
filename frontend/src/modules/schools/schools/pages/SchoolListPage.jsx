import { useEffect, useState } from "react";

import schoolService from "../services/schoolService";

const SchoolsListPage = () => {

    const [schools, setSchools] =
        useState([]);

    useEffect(() => {

        fetchSchools();

    }, []);

    const fetchSchools =
        async () => {

            const response =
                await schoolService.getSchools();

            setSchools(
                response.data.results ||
                response.data
            );
        };

    return (

        <div>

            <h2>Schools</h2>

            <table>

                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Code</th>
                    </tr>
                </thead>

                <tbody>

                    {schools.map(
                        (school) => (
                            <tr
                                key={school.id}
                            >
                                <td>
                                    {school.name}
                                </td>

                                <td>
                                    {school.code}
                                </td>
                            </tr>
                        )
                    )}

                </tbody>

            </table>

        </div>
    );
};

export default SchoolsListPage;