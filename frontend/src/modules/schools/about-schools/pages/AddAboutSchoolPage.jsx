import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import AboutSchoolForm from "../components/AboutSchoolForm";

import aboutSchoolService from "../services/aboutSchoolService";


const AddAboutSchoolPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            try {

                await aboutSchoolService
                    .createAboutSchool(data);

                toast.success(
                    "About School created successfully."
                );

                navigate(
                    "/dashboard/schools/about-schools"
                );

            } catch (error) {

                console.error(error);

                toast.error(
                    "Failed to create About School."
                );
            }
        };

    return (

        <div className="max-w-5xl mx-auto">

            <div className="bg-white rounded-xl shadow-sm border border-gray-200">

                <div className="border-b border-gray-200 px-6 py-5">

                    <h1 className="text-2xl font-bold text-gray-800">
                        Add About School
                    </h1>

                    <p className="mt-1 text-sm text-gray-500">
                        Enter the school's history, vision, and mission.
                    </p>

                </div>

                <div className="p-6">

                    <AboutSchoolForm
                        onSubmit={handleSubmit}
                    />

                </div>

            </div>

        </div>
    );
};

export default AddAboutSchoolPage;