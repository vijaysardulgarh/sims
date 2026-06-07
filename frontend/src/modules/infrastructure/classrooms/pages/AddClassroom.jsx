import {
    useState
} from "react";

import {
    useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import ClassroomForm from "../components/ClassroomForm";

import classroomService from "../services/classroomService";


// ============================================
// ADD CLASSROOM
// ============================================

const AddClassroom = () => {

    const navigate =
        useNavigate();

    const [loading, setLoading] =
        useState(false);

    // ========================================
    // SUBMIT
    // ========================================

    const handleSubmit = async (
        data
    ) => {

        try {

            setLoading(true);

            await classroomService.createClassroom(
                data
            );

            toast.success(
                "Classroom created successfully"
            );

            navigate(
                "/dashboard/infrastructure/classrooms"
            );

        } catch (error) {

            console.error(
                error
            );

            const errors =
                error?.response?.data;

            if (

                errors &&

                typeof errors ===
                    "object"
            ) {

                Object.entries(
                    errors
                ).forEach(

                    ([field, value]) => {

                        toast.error(

                            `${field}: ${Array.isArray(value)

                                ? value.join(", ")

                                : value}`
                        );
                    }
                );

            } else {

                toast.error(
                    "Failed to create classroom"
                );
            }

        } finally {

            setLoading(false);
        }
    };

    // ========================================
    // UI
    // ========================================

    return (

        <div className="space-y-6">

            <div>

                <h1
                    className="
                        text-3xl
                        font-bold
                        text-gray-800
                    "
                >
                    Add Classroom
                </h1>

                <p
                    className="
                        text-gray-500
                        mt-1
                    "
                >
                    Create a new classroom
                </p>

            </div>

            <ClassroomForm

                onSubmit={
                    handleSubmit
                }

                loading={
                    loading
                }
            />

        </div>
    );
};

export default AddClassroom;