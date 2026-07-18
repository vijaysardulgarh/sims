// src/modules/clusters/pages/ClusterViewPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    useParams,
    Link,
} from "react-router-dom";

import {
    getCluster,
} from "../services/clusterService";

const ClusterViewPage = () => {

    const { id } = useParams();

    const [cluster, setCluster] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        const fetchCluster = async () => {

            try {

                const data = await getCluster(id);

                setCluster(data);

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);

            }

        };

        fetchCluster();

    }, [id]);

    if (loading) {

        return (
            <div className="p-6">
                Loading...
            </div>
        );

    }

    if (!cluster) {

        return (
            <div className="p-6">
                Cluster not found.
            </div>
        );

    }

    return (

        <div className="max-w-4xl mx-auto p-6">

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-3xl font-bold">

                    {cluster.name}

                </h1>

                <Link
                    to={`/dashboard/clusters/${cluster.id}/edit`}
                    className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
                >
                    Edit
                </Link>

            </div>

            <div className="bg-white shadow rounded-lg p-6">

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                    {/* BASIC INFORMATION */}

                    <div>

                        <h2 className="text-lg font-semibold mb-3">

                            Basic Information

                        </h2>

                        <p><strong>Cluster Name:</strong> {cluster.name}</p>

                        <p><strong>Code:</strong> {cluster.code}</p>

                        <p><strong>Description:</strong> {cluster.description || "-"}</p>

                        <p>
                            <strong>Status:</strong>{" "}
                            <span
                                className={
                                    cluster.is_active
                                        ? "text-green-600"
                                        : "text-red-600"
                                }
                            >
                                {cluster.is_active
                                    ? "Active"
                                    : "Inactive"}
                            </span>
                        </p>

                    </div>

                    {/* CRC INFORMATION */}

                    <div>

                        <h2 className="text-lg font-semibold mb-3">

                            CRC Information

                        </h2>

                        <p><strong>Name:</strong> {cluster.crc_name}</p>

                        <p><strong>Designation:</strong> {cluster.crc_designation || "-"}</p>

                        <p><strong>Phone:</strong> {cluster.crc_phone || "-"}</p>

                        <p><strong>Email:</strong> {cluster.crc_email || "-"}</p>

                    </div>

                    {/* OFFICE CONTACT */}

                    <div className="md:col-span-2">

                        <h2 className="text-lg font-semibold mb-3">

                            Office Contact

                        </h2>

                        <p><strong>Email:</strong> {cluster.email || "-"}</p>

                        <p><strong>Phone:</strong> {cluster.phone || "-"}</p>

                        <p><strong>Address:</strong> {cluster.address || "-"}</p>

                    </div>

                </div>

            </div>

        </div>

    );

};

export default ClusterViewPage;