import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import PrincipalForm from "../components/PrincipalForm";

import principalService from "../services/principalService";


const EditPrincipalPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [principal, setPrincipal] = useState(null);

    const [loading, setLoading] = useState(true);

    const [saving, setSaving] = useState(false);

    useEffect(() => {

        fetchPrincipal();

    }, [id]);

    const fetchPrincipal = async () => {

        try {

            setLoading(true);

            const response =
                await principalService.getPrincipal(id);

            setPrincipal(response.data);

        } catch (error) {

            console.error(error);

            toast.error(
                "Unable to load principal."
            );

        } finally {

            setLoading(false);

        }

    };

    const handleSubmit = async (data) => {

        try {

            setSaving(true);

            await principalService.updatePrincipal(
                id,
                data
            );

            toast.success(
                "Principal updated successfully."
            );

            navigate(
                "/dashboard/schools/principals"
            );

        } catch (error) {

            console.error(error);

            toast.error(
                "Unable to update principal."
            );

        } finally {

            setSaving(false);

        }

    };

    if (loading) {

        return (

            <div className="text-center py-10">

                Loading...

            </div>

        );

    }

    return (

        <div className="max-w-5xl mx-auto space-y-6">

            <div>

                <h1
                    className="
                        text-3xl
                        font-bold
                        text-gray-900
                    "
                >
                    Edit Principal
                </h1>

                <p
                    className="
                        mt-1
                        text-gray-500
                    "
                >
                    Update principal information.
                </p>

            </div>

            <PrincipalForm
                initialData={principal}
                onSubmit={handleSubmit}
                loading={saving}
            />

        </div>

    );

};

export default EditPrincipalPage;