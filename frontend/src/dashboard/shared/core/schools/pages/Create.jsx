import {
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import Form from "../components/Form";

import schoolService from "../services/schoolService";

const Create = () => {

    const navigate = useNavigate();

    const [loading, setLoading] =
        useState(false);

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await schoolService.createSchool(data);

            navigate(
                "/dashboard/core/schools"
            );

        } finally {
            setLoading(false);
        }
    };

    return (

        <Form
            onSubmit={handleSubmit}
            loading={loading}
        />
    );
};

export default Create;