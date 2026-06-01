import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import Button
from "../../../../components/ui/Button";

import PageHeader
from "../../../../components/ui/PageHeader";

import BuildingForm
from "./BuildingForm";

import {
    createBuilding,
    getBuilding,
    updateBuilding,
} from "../services/buildingService";

const BuildingFormPage = () => {

    const navigate = useNavigate();

    const { id } = useParams();

    const isEdit = Boolean(id);

    const [loading, setLoading] =
        useState(false);

    const [formData, setFormData] =
        useState({

            name: "",

            code: "",

            description: "",

            number_of_floors: 1,

            is_active: true,

        });

    const handleChange = (e) => {

        setFormData((prev) => ({

            ...prev,

            [e.target.name]:
                e.target.value,

        }));

    };

    useEffect(() => {

        if (!isEdit) return;

        loadBuilding();

    }, [id]);

    const loadBuilding = async () => {

        try {

            setLoading(true);

            const response =
                await getBuilding(id);

            setFormData(
                response.data
            );

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };

    const handleSubmit =
        async (e) => {

            e.preventDefault();

            try {

                setLoading(true);

                if (isEdit) {

                    await updateBuilding(
                        id,
                        formData
                    );

                } else {

                    await createBuilding(
                        formData
                    );

                }

                navigate(
                    "/dashboard/buildings"
                );

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);

            }

        };

    return (

        <div className="space-y-6">

            <PageHeader

                title={
                    isEdit
                        ? "Edit Building"
                        : "Add Building"
                }

                subtitle={
                    isEdit
                        ? "Update building information"
                        : "Create a new building"
                }

                breadcrumbs={[

                    "Dashboard",

                    "Infrastructure",

                    "Buildings",

                    isEdit
                        ? "Edit"
                        : "Add",

                ]}

            />

            <div
                className="
                    bg-white
                    border
                    rounded-xl
                    shadow-sm
                    p-6
                "
            >

                <form
                    onSubmit={
                        handleSubmit
                    }
                    className="
                        space-y-6
                    "
                >

                    <BuildingForm

                        values={
                            formData
                        }

                        onChange={
                            handleChange
                        }

                    />

                    <div
                        className="
                            flex
                            justify-end
                            gap-3
                        "
                    >

                        <Button

                            type="button"

                            variant="secondary"

                            onClick={() =>
                                navigate(
                                    "/dashboard/buildings"
                                )
                            }

                        >
                            Cancel
                        </Button>

                        <Button
                            type="submit"
                            disabled={
                                loading
                            }
                        >
                            {loading
                                ? "Saving..."
                                : "Save Building"}
                        </Button>

                    </div>

                </form>

            </div>

        </div>

    );

};

export default BuildingFormPage;