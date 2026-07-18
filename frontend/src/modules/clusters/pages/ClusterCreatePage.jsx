// src/modules/clusters/pages/ClusterCreatePage.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";

import ClusterForm from "../components/ClusterForm";
import { createCluster } from "../services/clusterService";

const ClusterCreatePage = () => {

    const navigate = useNavigate();

    const [loading, setLoading] = useState(false);

    // =====================================
    // CREATE CLUSTER
    // =====================================

    const handleSubmit = async (formData) => {

        try {

            setLoading(true);

            await createCluster(formData);

            navigate("/dashboard/clusters");

        } catch (error) {

            console.error(error);

            alert(
                JSON.stringify(
                    error.response?.data || error.message,
                    null,
                    2
                )
            );

        } finally {

            setLoading(false);

        }
    };

    return (

        <div className="max-w-4xl mx-auto p-6">

            <h1 className="text-2xl font-bold mb-6">
                Create Cluster
            </h1>

            <ClusterForm
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>

    );
};

export default ClusterCreatePage;