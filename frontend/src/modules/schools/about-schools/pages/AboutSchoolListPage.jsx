import {
    useEffect,
    useState
} from "react";

import aboutSchoolService from "../services/aboutSchoolService";

const AboutSchoolListPage = () => {

    const [records, setRecords] =
        useState([]);

    useEffect(() => {

        fetchRecords();

    }, []);

    const fetchRecords =
        async () => {

            const response =
                await aboutSchoolService
                    .getAboutSchools();

            setRecords(
                response.data.results ||
                response.data
            );
        };

    return (

        <div>

            <h2>
                About Schools
            </h2>

            <table>

                <thead>

                    <tr>
                        <th>ID</th>
                        <th>School</th>
                    </tr>

                </thead>

                <tbody>

                    {records.map(
                        (record) => (

                            <tr
                                key={record.id}
                            >

                                <td>
                                    {record.id}
                                </td>

                                <td>
                                    {
                                        record.school_name
                                    }
                                </td>

                            </tr>
                        )
                    )}

                </tbody>

            </table>

        </div>
    );
};

export default AboutSchoolListPage;