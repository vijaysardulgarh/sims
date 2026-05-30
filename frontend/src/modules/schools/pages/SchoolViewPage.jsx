// src/modules/schools/pages/SchoolViewPage.jsx

import { useEffect, useState } from "react";

import { useParams } from "react-router-dom";

import {
    getSchool,
} from "../services/schoolService";

const SchoolViewPage = () => {

    const { id } = useParams();

    const [school, setSchool] =
        useState(null);

    useEffect(() => {

        const fetchSchool = async () => {

            const data =
                await getSchool(id);

            setSchool(data);
        };

        fetchSchool();

    }, [id]);

    if (!school) {

        return <p>Loading...</p>;
    }

    return (

        <div className="p-4">

            <h1 className="text-3xl font-bold">
                {school.name}
            </h1>

            {
                school.logo_url && (
                    <img
                        src={school.logo_url}
                        alt={school.name}
                        className="w-40 mt-4"
                    />
                )
            }

            <div className="mt-4 space-y-2">

                <p>
                    <strong>Code:</strong>
                    {school.code}
                </p>

                <p>
                    <strong>Email:</strong>
                    {school.email}
                </p>

                <p>
                    <strong>Phone:</strong>
                    {school.phone}
                </p>

                <p>
                    <strong>Address:</strong>
                    {school.address}
                </p>

            </div>

        </div>
    );
};

export default SchoolViewPage;