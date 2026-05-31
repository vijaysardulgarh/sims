import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import AboutSchoolForm from "../components/AboutSchoolForm";

import aboutSchoolService from "../services/aboutSchoolService";

const EditAboutSchoolPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [record, setRecord] =
        useState(null);

    useEffect(() => {

        fetchRecord();

    }, [id]);

    const fetchRecord =
        async () => {

            const response =
                await aboutSchoolService
                    .getAboutSchool(id);

            setRecord(
                response.data
            );
        };

    const handleSubmit =
        async (data) => {

            await aboutSchoolService
                .updateAboutSchool(
                    id,
                    data
                );

            navigate(
                "/dashboard/schools/about-schools"
            );
        };

    if (!record)
        return <p>Loading...</p>;

    return (

        <AboutSchoolForm
            initialData={record}
            onSubmit={handleSubmit}
        />
    );
};

export default EditAboutSchoolPage;