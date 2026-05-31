import { useNavigate } from "react-router-dom";

import AboutSchoolForm from "../components/AboutSchoolForm";

import aboutSchoolService from "../services/aboutSchoolService";

const AddAboutSchoolPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            await aboutSchoolService
                .createAboutSchool(data);

            navigate(
                "/dashboard/schools/about-schools"
            );
        };

    return (

        <AboutSchoolForm
            onSubmit={handleSubmit}
        />
    );
};

export default AddAboutSchoolPage;