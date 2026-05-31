import { useNavigate } from "react-router-dom";

import BranchForm from "../components/BranchForm";

import branchService from "../services/branchService";

const AddBranchPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            await branchService
                .createBranch(data);

            navigate(
                "/dashboard/schools/branches"
            );
        };

    return (

        <BranchForm
            onSubmit={handleSubmit}
        />
    );
};

export default AddBranchPage;