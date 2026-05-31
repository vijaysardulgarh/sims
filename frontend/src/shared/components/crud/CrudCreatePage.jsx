import { useState } from 'react';

import { useNavigate } from 'react-router-dom';

import api from '../../../services/api/axios';

const CrudCreatePage = ({
    title,
    endpoint,
    FormComponent,
    redirectPath,
}) => {

    const navigate =
        useNavigate();

    const [formData, setFormData] =
        useState({});

    const handleSubmit =
        async (e) => {

            e.preventDefault();

            try {

                await api.post(
                    endpoint,
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
                    Save
                </button>

            </form>

        </div>
    );
};

export default CrudCreatePage;