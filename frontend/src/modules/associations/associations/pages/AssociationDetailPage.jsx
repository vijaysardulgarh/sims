// ============================================
// IMPORTS
// ============================================

import {
    useEffect,
    useState
} from 'react';

import {
    useParams,
    useNavigate
} from 'react-router-dom';

import associationService from '../services/associationService';

// ============================================
// COMPONENT
// ============================================

const AssociationDetailPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [association, setAssociation] =
        useState(null);

    const [loading, setLoading] =
        useState(true);

    // ========================================
    // FETCH DETAIL
    // ========================================

    useEffect(() => {

        const fetchDetail = async () => {

            try {

                const response =
                    await associationService.getById(
                        id
                    );

                console.log(
                    'Association Detail:',
                    response
                );

                setAssociation(
                    response?.data || response
                );

            }

            catch (error) {

                console.error(
                    'Association Detail Error:',
                    error
                );

            }

            finally {

                setLoading(
                    false
                );

            }

        };

        fetchDetail();

    }, [id]);

    // ========================================
    // LOADING
    // ========================================

    if (loading) {

        return (

            <div className="p-6">

                Loading...

            </div>

        );

    }

    // ========================================
    // NOT FOUND
    // ========================================

    if (!association) {

        return (

            <div className="p-6">

                Association not found

            </div>

        );

    }

    // ========================================
    // DEBUG
    // ========================================

    console.log(
        'DETAIL ASSOCIATION:',
        association
    );

    // ========================================
    // UI
    // ========================================

    return (

        <div className="p-6">

            <div className="bg-white rounded-2xl shadow p-6 space-y-4">

                <h1 className="text-3xl font-bold">

                    {association.name || '-'}

                </h1>

                <p>

                    <strong>
                        Type:
                    </strong>

                    {' '}

                    {
                        association.association_type_display ||
                        association.association_type ||
                        '-'
                    }

                </p>

                <p>

                    <strong>
                        Status:
                    </strong>

                    {' '}

                    {
                        association.status_display ||
                        association.status ||
                        '-'
                    }

                </p>

                <p>

                    <strong>
                        Description:
                    </strong>

                    {' '}

                    {
                        association.description ||
                        '-'
                    }

                </p>

                <p>

                    <strong>
                        Tasks:
                    </strong>

                    {' '}

                    {
                        association.tasks ||
                        '-'
                    }

                </p>

                <p>

                    <strong>
                        Chairperson:
                    </strong>

                    {' '}

                    {
                        association.chairperson_name ||
                        '-'
                    }

                </p>

                <div className="flex gap-3 pt-4">

                    <button

                        onClick={() =>
                            navigate(
                                '/dashboard/associations/associations'
                            )
                        }

                        className="
                            bg-gray-600
                            text-white
                            px-5
                            py-2
                            rounded-xl
                        "
                    >
                        Back
                    </button>

                    <button

                        onClick={() => {

                            console.log(
                                'Association:',
                                association
                            );

                            if (
                                !association?.id
                            ) {

                                alert(
                                    'Association ID not found'
                                );

                                return;

                            }

                            navigate(
                                `/dashboard/associations/associations/edit/${association.id}`
                            );

                        }}

                        className="
                            bg-blue-600
                            text-white
                            px-5
                            py-2
                            rounded-xl
                        "
                    >
                        Edit
                    </button>

                </div>

            </div>

        </div>

    );

};

export default AssociationDetailPage;