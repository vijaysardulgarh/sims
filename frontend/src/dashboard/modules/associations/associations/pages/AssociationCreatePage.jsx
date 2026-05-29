// ============================================
// IMPORTS
// ============================================

import { useNavigate } from 'react-router-dom';

import { useState } from 'react';

import associationService from '../services/associationService';

import AssociationForm from '../components/AssociationForm';

// ============================================
// COMPONENT
// ============================================

const AssociationCreatePage = () => {

    const navigate = useNavigate();

    const [loading, setLoading] = useState(false);

    // ========================================
    // HANDLE SUBMIT
    // ========================================

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await associationService.create(data);

            navigate(
                '/dashboard/associations/associations'
            );
        }

        catch (error) {

            console.error(error);
        }

        finally {

            setLoading(false);
        }
    };

    return (

        <div className="p-6">

            <div className="bg-white p-6 rounded-2xl shadow max-w-3xl">

                <h1 className="text-3xl font-bold mb-6">
                    Create Association
                </h1>

                <AssociationForm
                    onSubmit={handleSubmit}
                    loading={loading}
                />

            </div>

        </div>

    );
};

export default AssociationCreatePage;