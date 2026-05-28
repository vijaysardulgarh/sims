// src/modules/clusters/pages/ClusterViewPage.jsx

import {
    useEffect,
    useState,
} from "react";

import { useParams } from "react-router-dom";

import {
    getCluster,
} from "../services/clusterService";

const ClusterViewPage = () => {

    const { id } = useParams();

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

    if (!cluster) {

        return <p>Loading...</p>;
    }

    return (

        <div className="p-4">

            <h1 className="text-3xl font-bold">
                {cluster.name}
            </h1>

            {
                cluster.logo_url && (

                    <img
                        src={cluster.logo_url}
                        alt={cluster.name}
                        className="w-40 mt-4"
                    />
                )
            }

            <div className="mt-4 space-y-2">

                <p>
                    <strong>Code:</strong>
                    {" "}
                    {cluster.code}
                </p>

                <p>
                    <strong>Email:</strong>
                    {" "}
                    {cluster.email}
                </p>

                <p>
                    <strong>Phone:</strong>
                    {" "}
                    {cluster.phone}
                </p>

                <p>
                    <strong>Timezone:</strong>
                    {" "}
                    {cluster.timezone}
                </p>

            </div>

        </div>
    );
};

export default ClusterViewPage;