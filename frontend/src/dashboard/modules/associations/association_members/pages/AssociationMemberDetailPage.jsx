import { useEffect, useState } from 'react';
import {
    Link,
    useParams,
} from 'react-router-dom';

import associationMemberService from '../services/associationMemberService';

const AssociationMemberDetailPage = () => {

    const { id } =
        useParams();

    const [member, setMember] =
        useState(null);

    useEffect(() => {

        loadMember();

    }, []);

    const loadMember = async () => {

        const response =
            await associationMemberService.getById(
                id
            );

        setMember(
            response.data.data
        );
    };

    if (!member)
        return <div>Loading...</div>;

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-4">
                Member Detail
            </h1>

            <p>
                Association:
                {member.association_name}
            </p>

            <p>
                Staff:
                {member.staff_name}
            </p>

            <p>
                Designation:
                {member.designation}
            </p>

            <p>
                Email:
                {member.email}
            </p>

            <p>
                Phone:
                {member.phone_number}
            </p>

            <Link
                to="/dashboard/associations/association_members"
                className="inline-block mt-4 px-4 py-2 bg-gray-600 text-white rounded"
            >
                Back
            </Link>

        </div>
    );
};

export default AssociationMemberDetailPage;