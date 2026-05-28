// src/modules/schools/pages/SchoolsListPage.jsx

import { useEffect, useState } from "react";

import {
    getSchools,
    deleteSchool,
} from "../services/schoolService";

import { Link } from "react-router-dom";

const SchoolsListPage = () => {

    const [schools, setSchools] =
        useState([]);

    // =====================================================
    // FETCH SCHOOLS
    // =====================================================

    const fetchSchools = async () => {

        try {

            const data =
                await getSchools();

            console.log(
                "Schools Data:",
                data
            );

            // GenericAPIView returns array directly

            setSchools(
                Array.isArray(data)
                    ? data
                    : []
            );

        } catch (error) {

            console.error(error);
        }
    };

    // =====================================================
    // LOAD
    // =====================================================

    useEffect(() => {

        fetchSchools();

    }, []);

    // =====================================================
    // DELETE
    // =====================================================

    const handleDelete = async (id) => {

        const confirmed = window.confirm(
            "Delete this school?"
        );

        if (!confirmed) return;

        try {

            await deleteSchool(id);

            fetchSchools();

        } catch (error) {

            console.error(error);
        }
    };

    // =====================================================
    // JSX
    // =====================================================

    return (

        <div className="p-4">

            {/* HEADER */}

            <div className="flex justify-between mb-4">

                <h1 className="text-2xl font-bold">
                    Schools
                </h1>

                <Link
                    to="/dashboard/schools/create"
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                    Add School
                </Link>

            </div>

            {/* TABLE */}

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
                            City
                        </th>

                        <th className="p-2">
                            Actions
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        Array.isArray(
                            schools
                        ) &&

                        schools.length > 0 ? (

                            schools.map((school) => (

                                <tr
                                    key={school.id}
                                    className="border-t"
                                >

                                    <td className="p-2">
                                        {school.name}
                                    </td>

                                    <td className="p-2">
                                        {school.code}
                                    </td>

                                    <td className="p-2">
                                        {school.city}
                                    </td>

                                    <td className="p-2 space-x-2">

                                        <Link
                                            to={`/dashboard/schools/${school.id}`}
                                            className="text-blue-500"
                                        >
                                            View
                                        </Link>

                                        <Link
                                            to={`/dashboard/schools/${school.id}/edit`}
                                            className="text-green-500"
                                        >
                                            Edit
                                        </Link>

                                        <button
                                            onClick={() =>
                                                handleDelete(
                                                    school.id
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
                                    No schools found
                                </td>

                            </tr>
                        )
                    }

                </tbody>

            </table>

        </div>
    );
};

export default SchoolsListPage;