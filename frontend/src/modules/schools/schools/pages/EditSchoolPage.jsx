import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import SchoolForm from "../components/SchoolForm";

import schoolService from "../services/schoolService";

const EditSchoolPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [school, setSchool] =
        useState(null);

    useEffect(() => {

        fetchSchool();

    }, [id]);

    const fetchSchool =
        async () => {

            const response =
                await schoolService
                    .getSchool(id);

            setSchool(
                response.data
            );
        };

    const handleSubmit =
        async (data) => {

            await schoolService
                .updateSchool(
                    id,
                    data
                );

            navigate(
                "/dashboard/schools/schools"
            );
        };

    if (!school)
        return <p>Loading...</p>;

    return (

        <SchoolForm
            initialData={school}
            onSubmit={handleSubmit}
        />
    );
};

export default EditSchoolPage;