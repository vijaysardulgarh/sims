import {
    useEffect,
    useState,
} from 'react';

import {
    useNavigate,
    useParams,
} from 'react-router-dom';

import api from '../../../services/api/axios';

const CrudEditPage = ({
    title,
    endpoint,
    FormComponent,
    redirectPath,
}) => {

    const { id } =
        useParams();

    const navigate =
        useNavigate();

    const [formData, setFormData] =
        useState({});

    useEffect(() => {

        loadRecord();

    }, []);

    const loadRecord =
        async () => {

            try {

                const response =
                    await api.get(
                        `${endpoint}${id}/`
                    );

                setFormData(
                    response.data
                );

            } catch (error) {

                console.error(error);
            }
        };

    const handleSubmit =
        async (e) => {

            e.preventDefault();

            try {

                await api.put(
                    `${endpoint}${id}/`,
                    formData
                );

                navigate(
                    redirectPath
                );

            } catch (error) {

                console.error(error);
            }
        };

    return (
        <div className="container-fluid">

            <h3 className="mb-3">
                {title}
            </h3>

            <form
                onSubmit={
                    handleSubmit
                }
            >

                <FormComponent
                    formData={
                        formData
                    }
                    setFormData={
                        setFormData
                    }
                />

                <button
                    type="submit"
                    className="
                        btn
                        btn-primary
                    "
                >
                    Update
                </button>

            </form>

        </div>
    );
};

export default CrudEditPage;