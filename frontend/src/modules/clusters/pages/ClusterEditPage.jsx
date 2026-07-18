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

    const [cluster, setCluster] = useState(null);

    const [loading, setLoading] = useState(false);

    const [pageLoading, setPageLoading] =
        useState(true);

    // =====================================
    // FETCH CLUSTER
    // =====================================

    useEffect(() => {

        const fetchCluster = async () => {

            try {

                const data = await getCluster(id);

                setCluster(data);

            } catch (error) {

                console.error(error);

                alert(
                    "Failed to load cluster."
                );

            } finally {

                setPageLoading(false);

            }

        };

        fetchCluster();

    }, [id]);

    // =====================================
    // UPDATE CLUSTER
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            setLoading(true);

            await updateCluster(
                id,
                formData
            );

            navigate(
                "/dashboard/clusters"
            );

        } catch (error) {

            console.error(error);

            alert(

                JSON.stringify(

                    error.response?.data ||
                    error.message,

                    null,

                    2
                )
            );

        } finally {

            setLoading(false);

        }

    };

    if (pageLoading) {

        return (

            <div className="p-6">

                Loading...

            </div>

        );

    }

    return (

        <div className="max-w-4xl mx-auto p-6">

            <h1 className="text-2xl font-bold mb-6">

                Edit Cluster

            </h1>

            <ClusterForm

                initialData={cluster}

                onSubmit={handleSubmit}

                loading={loading}

            />

        </div>

    );

};

export default ClusterEditPage;