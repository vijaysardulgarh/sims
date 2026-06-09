import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import Form from "../components/Form";

import transportAssignmentService from "../services/transportAssignmentService";


const Edit = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [assignment, setAssignment] =
        useState(null);

    const [loading, setLoading] =
        useState(false);

    useEffect(() => {

        loadAssignment();

    }, []);

    const loadAssignment = async () => {

        try {

            const response =
                await transportAssignmentService.getAssignment(id);

            setAssignment(response);

        } catch (error) {

            toast.error(
                "Failed to load assignment"
            );
        }
    };

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await transportAssignmentService.updateAssignment(
                id,
                data
            );

            toast.success(
                "Assignment updated successfully"
            );

            navigate(
                "/dashboard/transport/transport-assignments"
            );

        } catch (error) {

            toast.error(
                "Failed to update assignment"
            );

        } finally {

            setLoading(false);
        }
    };

    if (!assignment) {

        return (
            <div>
                Loading assignment...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Edit Assignment

            </h1>

            <Form
                initialData={assignment}
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Edit;