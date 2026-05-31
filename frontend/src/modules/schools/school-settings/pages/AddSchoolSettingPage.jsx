import { useNavigate } from "react-router-dom";

import SchoolSettingForm from "../components/SchoolSettingForm";

import schoolSettingService from "../services/schoolSettingService";

const AddSchoolSettingPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            await schoolSettingService
                .createSchoolSetting(data);

            navigate(
                "/dashboard/schools/school-settings"
            );
        };

    return (

        <SchoolSettingForm
            onSubmit={handleSubmit}
        />
    );
};

export default AddSchoolSettingPage;