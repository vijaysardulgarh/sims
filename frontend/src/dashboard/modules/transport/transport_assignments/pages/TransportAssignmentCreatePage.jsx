import {
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import Form from "../components/Form";

import transportAssignmentService from "../services/transportAssignmentService";


const Create = () => {

    const navigate = useNavigate();

    const [loading, setLoading] =
        useState(false);

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await transportAssignmentService.createAssignment(
                data
            );

            toast.success(
                "Assignment created successfully"
            );

            navigate(
                "/dashboard/transport/transport-assignments"
            );

        } catch (error) {

            toast.error(
                "Failed to create assignment"
            );

        } finally {

            setLoading(false);
        }
    };

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Create Assignment

            </h1>

            <Form
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Create;