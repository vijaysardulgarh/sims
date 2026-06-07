import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import Form from "../components/Form";

import schoolService from "../services/schoolService";

const Edit = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [school, setSchool] =
        useState(null);

    const [loading, setLoading] =
        useState(false);

    useEffect(() => {
        loadSchool();
    }, []);

    const loadSchool = async () => {

        const response =
            await schoolService.getSchool(id);

        setSchool(response);
    };

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await schoolService.updateSchool(
                id,
                data
            );

            navigate(
                "/dashboard/core/schools"
            );

        } finally {
            setLoading(false);
        }
    };

    if (!school) {
        return <div>Loading...</div>;
    }

    return (

        <Form
            initialData={school}
            onSubmit={handleSubmit}
            loading={loading}
        />
    );
};

export default Edit;