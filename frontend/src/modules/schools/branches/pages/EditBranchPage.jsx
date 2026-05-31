import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import BranchForm from "../components/BranchForm";

import branchService from "../services/branchService";

const EditBranchPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [branch, setBranch] =
        useState(null);

    useEffect(() => {

        fetchBranch();

    }, [id]);

    const fetchBranch =
        async () => {

            const response =
                await branchService
                    .getBranch(id);

            setBranch(
                response.data
            );
        };

    const handleSubmit =
        async (data) => {

            await branchService
                .updateBranch(
                    id,
                    data
                );

            navigate(
                "/dashboard/schools/branches"
            );
        };

    if (!branch)
        return <p>Loading...</p>;

    return (

        <BranchForm
            initialData={branch}
            onSubmit={handleSubmit}
        />
    );
};

export default EditBranchPage;