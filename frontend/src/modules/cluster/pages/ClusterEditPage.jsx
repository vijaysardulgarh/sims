// src/modules/clusters/pages/ClusterEditPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import ClusterForm from "../components/ClusterForm";

import {
    getCluster,
    updateCluster,
} from "../services/clusterService";

const ClusterEditPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [cluster, setCluster] =
        useState(null);

    useEffect(() => {

        const fetchCluster =
            async () => {

                const data =
                    await getCluster(id);

                setCluster(data);
            };

        fetchCluster();

    }, [id]);

    const handleSubmit = async (
        formData
    ) => {

        try {

            await updateCluster(
                id,
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

    if (!cluster) {

        return <p>Loading...</p>;
    }

    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">
                Edit Cluster
            </h1>

            <ClusterForm
                initialData={cluster}
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default ClusterEditPage;