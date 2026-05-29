import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import associationMemberService from '../services/associationMemberService';
import AssociationMemberTable from '../components/AssociationMemberTable';

const AssociationMemberListPage = () => {

    const [members, setMembers] =
        useState([]);

    useEffect(() => {

        fetchMembers();

    }, []);

    const fetchMembers = async () => {

        const response =
            await associationMemberService.getAll();

        setMembers(
            response.data.data || []
        );
    };

    const handleDelete = async (id) => {

        await associationMemberService.delete(
            id
        );

        fetchMembers();
    };

    return (

        <div className="p-6">

            <div className="flex justify-between mb-6">

                <h1 className="text-2xl font-bold">
                    Association Members
                </h1>

                <Link
                    to="/dashboard/associations/association_members/create"
                    className="px-4 py-2 bg-blue-600 text-white rounded"
                >
                    Add Member
                </Link>

            </div>

            <AssociationMemberTable
                members={members}
                onDelete={handleDelete}
            />

        </div>
    );
};

export default AssociationMemberListPage;