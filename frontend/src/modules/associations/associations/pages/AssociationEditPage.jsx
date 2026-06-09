// ============================================
// IMPORTS
// ============================================

import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import associationService from "../services/associationService";

import AssociationForm from "../components/AssociationForm";

// ============================================
// COMPONENT
// ============================================

const AssociationEditPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [association, setAssociation] =
        useState({});

    const [loading, setLoading] =
        useState(false);

    const [pageLoading, setPageLoading] =
        useState(true);

    // ========================================
    // FETCH DETAIL
    // ========================================

    useEffect(() => {

        fetchAssociation();

    }, [id]);

    const fetchAssociation = async () => {

        try {

            const response =
                await associationService.getAssociation(
                    id
                );

            console.log(
                "Association Detail:",
                response
            );

            setAssociation(
                response.data
            );

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setPageLoading(false);

        }
    };

    // ========================================
    // UPDATE
    // ========================================

    const handleSubmit = async (
        data
    ) => {

        try {

            setLoading(true);

            await associationService.updateAssociation(
                id,
                data
            );

            navigate(
                "/dashboard/associations/associations"
            );

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }
    };

    // ========================================
    // LOADING
    // ========================================

    if (pageLoading) {

        return (

            <div className="p-6">

                Loading...

            </div>

        );
    }

    // ========================================
    // UI
    // ========================================

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