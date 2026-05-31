import { useNavigate } from "react-router-dom";

import PrincipalForm from "../components/PrincipalForm";

import principalService from "../services/principalService";

const AddPrincipalPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            await principalService
                .createPrincipal(data);

            navigate(
                "/dashboard/schools/principals"
            );
        };

    return (

        <PrincipalForm
            onSubmit={handleSubmit}
        />
    );
};

export default AddPrincipalPage;