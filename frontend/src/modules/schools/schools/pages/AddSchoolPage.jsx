import { useNavigate } from "react-router-dom";

import schoolService from "../services/schoolService";

import SchoolForm from "../components/SchoolForm";

const AddSchoolPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            await schoolService
                .createSchool(data);

            navigate(
                "/dashboard/schools/schools"
            );
        };

    return (

        <SchoolForm
            onSubmit={handleSubmit}
        />
    );
};

export default AddSchoolPage;