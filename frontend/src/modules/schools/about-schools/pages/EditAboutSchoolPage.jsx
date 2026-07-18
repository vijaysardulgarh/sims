import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import AboutSchoolForm from "../components/AboutSchoolForm";

import aboutSchoolService from "../services/aboutSchoolService";


const EditAboutSchoolPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [record, setRecord] =
        useState(null);

    const [loading, setLoading] =
        useState(true);

    useEffect(() => {

        fetchRecord();

    }, [id]);

    const fetchRecord =
        async () => {

            try {

                const response =
                    await aboutSchoolService
                        .getAboutSchool(id);

                setRecord(
                    response.data
                );

            } catch (error) {

                console.error(error);

                toast.error(
                    "Failed to load About School."
                );

                navigate(
                    "/dashboard/schools/about-schools"
                );

            } finally {

                setLoading(false);
            }
        };

    const handleSubmit =
        async (data) => {

            try {

                await aboutSchoolService
                    .updateAboutSchool(
                        id,
                        data
                    );

                toast.success(
                    "About School updated successfully."
                );

                navigate(
                    "/dashboard/schools/about-schools"
                );

            } catch (error) {

                console.error(error);

                toast.error(
                    "Failed to update About School."
                );
            }
        };

    if (loading)
        return <p>Loading...</p>;

    return (

        <AboutSchoolForm
            initialData={record}
            onSubmit={handleSubmit}
        />
    );
};

export default EditAboutSchoolPage;