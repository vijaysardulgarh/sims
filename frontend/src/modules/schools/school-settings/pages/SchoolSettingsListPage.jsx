import {
    useEffect,
    useState,
} from "react";

import schoolSettingService from "../services/schoolSettingService";

const SchoolSettingsListPage = () => {

    const [settings, setSettings] =
        useState([]);

    useEffect(() => {

        fetchSettings();

    }, []);

    const fetchSettings =
        async () => {

            const response =
                await schoolSettingService
                    .getSchoolSettings();

            setSettings(
                response.data.results ||
                response.data
            );
        };

    return (

        <div>

            <h2>
                School Settings
            </h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>School</th>

                        <th>Attendance</th>

                        <th>Grading</th>

                    </tr>

                </thead>

                <tbody>

                    {settings.map(
                        (setting) => (

                            <tr
                                key={setting.id}
                            >

                                <td>
                                    {setting.id}
                                </td>

                                <td>
                                    {
                                        setting.school_name
                                    }
                                </td>

                                <td>
                                    {
                                        setting.attendance_type
                                    }
                                </td>

                                <td>
                                    {
                                        setting.grading_system
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

export default SchoolSettingsListPage;