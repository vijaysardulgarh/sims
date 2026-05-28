// ============================================
// IMPORTS
// ============================================

import { useEffect, useState } from 'react';

import {
    useNavigate,
    useParams,
} from 'react-router-dom';

import associationService from '../services/associationService';

import AssociationForm from '../components/AssociationForm';

// ============================================
// COMPONENT
// ============================================

const AssociationEditPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [association, setAssociation] = useState(null);

    const [loading, setLoading] = useState(false);

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

    // ========================================
    // HANDLE SUBMIT
    // ========================================

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await associationService.update(
                id,
                data
            );

            navigate('/dashboard/associations');
        }

        catch (error) {

            console.error(error);
        }

        finally {

            setLoading(false);
        }
    };

    if (!association) {

        return <div>Loading...</div>;
    }

    return (

        <div className="p-6">

            <div className="bg-white p-6 rounded-2xl shadow max-w-3xl">

                <h1 className="text-3xl font-bold mb-6">
                    Edit Association
                </h1>

                <AssociationForm
                    initialData={association}
                    onSubmit={handleSubmit}
                    loading={loading}
                />
            </div>
        </div>
    );
};

export default AssociationEditPage;