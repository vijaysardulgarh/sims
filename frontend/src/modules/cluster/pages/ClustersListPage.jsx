// src/modules/clusters/pages/ClustersListPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    getClusters,
    deleteCluster,
} from "../services/clusterService";

import { Link } from "react-router-dom";

const ClustersListPage = () => {

    const [clusters, setClusters] =
        useState([]);

    const fetchClusters = async () => {

        try {

            const data =
                await getClusters();

            setClusters(
                Array.isArray(data)
                    ? data
                    : data.results || []
            );

        } catch (error) {

            console.error(error);
        }
    };

    useEffect(() => {

        fetchClusters();

    }, []);

    const handleDelete = async (
        id
    ) => {

        const confirmed = window.confirm(
            "Delete this cluster?"
        );

        if (!confirmed) return;

        try {

            await deleteCluster(id);

            fetchClusters();

        } catch (error) {

            console.error(error);
        }
    };

    return (

        <div className="p-4">

            <div className="flex justify-between mb-4">

                <h1 className="text-2xl font-bold">
                    Clusters
                </h1>

                <Link
                    to="/dashboard/clusters/create"
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                    Add Cluster
                </Link>

            </div>

            <table className="w-full border">

                <thead>

                    <tr className="bg-gray-100">

                        <th className="p-2">
                            Name
                        </th>

                        <th className="p-2">
                            Code
                        </th>

                        <th className="p-2">
                            Email
                        </th>

                        <th className="p-2">
                            Actions
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        clusters.length > 0 ? (

                            clusters.map((cluster) => (

                                <tr
                                    key={cluster.id}
                                    className="border-t"
                                >

                                    <td className="p-2">
                                        {cluster.name}
                                    </td>

                                    <td className="p-2">
                                        {cluster.code}
                                    </td>

                                    <td className="p-2">
                                        {cluster.email}
                                    </td>

                                    <td className="p-2 space-x-2">

                                        <Link
                                            to={`/dashboard/clusters/${cluster.id}`}
                                            className="text-blue-500"
                                        >
                                            View
                                        </Link>

                                        <Link
                                            to={`/dashboard/clusters/${cluster.id}/edit`}
                                            className="text-green-500"
                                        >
                                            Edit
                                        </Link>

                                        <button
                                            onClick={() =>
                                                handleDelete(
                                                    cluster.id
                                                )
                                            }
                                            className="text-red-500"
                                        >
                                            Delete
                                        </button>

                                    </td>

                                </tr>
                            ))

                        ) : (

                            <tr>

                                <td
                                    colSpan="4"
                                    className="p-4 text-center"
                                >
                                    No clusters found
                                </td>

                            </tr>
                        )
                    }

                </tbody>

            </table>

        </div>
    );
};

export default ClustersListPage;