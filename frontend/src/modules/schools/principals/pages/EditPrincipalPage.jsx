import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import PrincipalForm from "../components/PrincipalForm";

import principalService from "../services/principalService";

const EditPrincipalPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [principal, setPrincipal] =
        useState(null);

    useEffect(() => {

        fetchPrincipal();

    }, [id]);

    const fetchPrincipal =
        async () => {

            const response =
                await principalService
                    .getPrincipal(id);

            setPrincipal(
                response.data
            );
        };

    const handleSubmit =
        async (data) => {

            await principalService
                .updatePrincipal(
                    id,
                    data
                );

            navigate(
                "/dashboard/schools/principals"
            );
        };

    if (!principal)
        return <p>Loading...</p>;

    return (

        <PrincipalForm
            initialData={principal}
            onSubmit={handleSubmit}
        />
    );
};

export default EditPrincipalPage;