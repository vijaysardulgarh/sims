// ============================================
// IMPORTS
// ============================================

import { useEffect, useState } from 'react';

import { Link } from 'react-router-dom';

import associationService from '../services/associationService';

import AssociationTable from '../components/AssociationTable';

// ============================================
// COMPONENT
// ============================================

const AssociationListPage = () => {

    const [associations, setAssociations] = useState([]);

    const [loading, setLoading] = useState(true);

    // ========================================
    // FETCH ASSOCIATIONS
    // ========================================

    const fetchAssociations = async () => {

        try {

            const response = await (
                associationService.getAll()
            );

            console.log(
                'Association API Response:',
                response
            );

            setAssociations(

                Array.isArray(
                    response?.data
                )

                    ? response.data

                    : []
            );
        }

        catch (error) {

            console.error(error);

            setAssociations([]);
        }

        finally {

            setLoading(false);
        }
    };

    useEffect(() => {

        fetchAssociations();

    }, []);

    // ========================================
    // DELETE
    // ========================================

    const handleDelete = async (id) => {

        const confirmed = window.confirm(
            'Delete association?'
        );

        if (!confirmed) return;

        try {

            await associationService.delete(id);

            fetchAssociations();
        }

        catch (error) {

            console.error(error);
        }
    };

    if (loading) {

        return (
            <div>
                Loading...
            </div>
        );
    }

    return (

        <div className="p-6 space-y-6">

            <div className="flex items-center justify-between">

                <h1 className="text-3xl font-bold">
                    Associations
                </h1>

                <Link
                    to="create"
                    className="bg-black text-white px-5 py-3 rounded-xl"
                >
                    Create Association
                </Link>

            </div>

            <AssociationTable

                associations={
                    Array.isArray(
                        associations
                    )
                        ? associations
                        : []
                }

                onDelete={handleDelete}
            />

        </div>
    );
};

export default AssociationListPage;