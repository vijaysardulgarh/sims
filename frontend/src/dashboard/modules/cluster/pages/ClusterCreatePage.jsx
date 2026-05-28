// src/modules/clusters/pages/ClusterCreatePage.jsx

import { useNavigate } from "react-router-dom";

import ClusterForm from "../components/ClusterForm";

import {
    createCluster,
} from "../services/clusterService";

const ClusterCreatePage = () => {

    const navigate = useNavigate();

    const handleSubmit = async (
        formData
    ) => {

        try {

            await createCluster(
                formData
            );

            navigate(
                "/dashboard/clusters"
            );

        } catch (error) {

            alert(

                JSON.stringify(

                    error.response?.data,

                    null,

                    2
                )
            );
        }
    };

    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">
                Create Cluster
            </h1>

            <ClusterForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default ClusterCreatePage;