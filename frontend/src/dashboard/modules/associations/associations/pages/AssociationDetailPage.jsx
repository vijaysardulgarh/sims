// ============================================
// IMPORTS
// ============================================

import { useEffect, useState } from 'react';

import { useParams } from 'react-router-dom';

import associationService from '../services/associationService';

// ============================================
// COMPONENT
// ============================================

const AssociationDetailPage = () => {

    const { id } = useParams();

    const [association, setAssociation] = useState(null);

    // ========================================
    // FETCH DETAIL
    // ========================================

    useEffect(() => {

        const fetchDetail = async () => {

            try {

                const response = await (
                    associationService.getById(id)
                );

                setAssociation(
                    response.data
                );
            }

            catch (error) {

                console.error(error);
            }
        };

        fetchDetail();

    }, [id]);

    if (!association) {

        return <div>Loading...</div>;
    }

    return (

        <div className="p-6">

            <div className="bg-white rounded-2xl shadow p-6 space-y-4">

                <h1 className="text-3xl font-bold">
                    {association.name}
                </h1>

                <p>
                    <strong>Type:</strong>
                    {' '}
                    {association.association_type}
                </p>

                <p>
                    <strong>Status:</strong>
                    {' '}
                    {association.status}
                </p>

                <p>
                    <strong>Description:</strong>
                    {' '}
                    {association.description}
                </p>

                <p>
                    <strong>Tasks:</strong>
                    {' '}
                    {association.tasks}
                </p>

                <p>
                    <strong>Chairperson:</strong>
                    {' '}
                    {association.chairperson}
                </p>
            </div>
        </div>
    );
};

export default AssociationDetailPage;