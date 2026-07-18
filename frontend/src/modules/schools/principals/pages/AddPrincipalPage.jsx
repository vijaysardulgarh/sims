import { useState } from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import PrincipalForm from "../components/PrincipalForm";

import principalService from "../services/principalService";


const AddPrincipalPage = () => {

    const navigate = useNavigate();

    const [loading, setLoading] = useState(false);

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await principalService.createPrincipal(data);

            toast.success(
                "Principal added successfully."
            );

            navigate(
                "/dashboard/schools/principals"
            );

        } catch (error) {

            console.error(error);

            toast.error(
                "Unable to add principal."
            );

        } finally {

            setLoading(false);

        }

    };

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
                    Add Principal
                </h1>

                <p
                    className="
                        mt-1
                        text-gray-500
                    "
                >
                    Create a new principal record.
                </p>

            </div>

            <PrincipalForm
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>

    );

};

export default AddPrincipalPage;