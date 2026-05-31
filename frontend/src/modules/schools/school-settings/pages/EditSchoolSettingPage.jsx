import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import SchoolSettingForm from "../components/SchoolSettingForm";

import schoolSettingService from "../services/schoolSettingService";

const EditSchoolSettingPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [setting, setSetting] =
        useState(null);

    useEffect(() => {

        fetchSetting();

    }, [id]);

    const fetchSetting =
        async () => {

            const response =
                await schoolSettingService
                    .getSchoolSetting(id);

            setSetting(
                response.data
            );
        };

    const handleSubmit =
        async (data) => {

            await schoolSettingService
                .updateSchoolSetting(
                    id,
                    data
                );

            navigate(
                "/dashboard/schools/school-settings"
            );
        };

    if (!setting)
        return <p>Loading...</p>;

    return (

        <SchoolSettingForm
            initialData={setting}
            onSubmit={handleSubmit}
        />
    );
};

export default EditSchoolSettingPage;